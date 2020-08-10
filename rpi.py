import RPi.GPIO as GPIO
import time

# Assign pin numbers for PI
pinTrigger = 18  # pin 12
pinEcho = 24  # Pin 18

# Difference between two epochs in seconds


def getTimeDiff(start, end):
    return round(end - start)

# Set the initial configuration for PI


def initPI():
    # set gpio Mode to BCM (BOARD / BCM)
    # Use the command "pinout" in the terminal to print out the pin numbering
    # More details in https://pinout.xyz/
    GPIO.setmode(GPIO.BCM)

    # output pin to initiate sensor and send a signal
    GPIO.setup(pinTrigger, GPIO.OUT)

    # Input pin to recieve sigal
    GPIO.setup(pinEcho, GPIO.IN)

    # Set the trigger to low so that it doesn't send a signal until it's
    # settled down
    GPIO.output(pinTrigger, False)
    time.sleep(2)


def getDistance(signalTimeout):
    # set Trigger to HIGH to send a signal
    GPIO.output(pinTrigger, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)

    triggerTime = time.time()
    # record time of trigger
    while GPIO.input(pinEcho) == 0:
        startTime = time.time()
        # Loop until signalTimeout seconds and exit to avoid infinite loop due
        # to sensor/connection issues
        if getTimeDiff(triggerTime, startTime) > signalTimeout:
            return -101

    triggerTime = time.time()
    # record the time of receival
    while GPIO.input(pinEcho) == 1:
        stopTime = time.time()
        # Loop until signalTimeout seconds and exit to avoid infinite loop due
        # to sensor/connection issues
        if getTimeDiff(triggerTime, stopTime) > signalTimeout:
            return -201

    # time difference between start and arrival
    timeDiff = stopTime - startTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because to and fro
    distance = round((timeDiff * 34300) / 2, 2)

    return distance


def cleanup():
    GPIO.cleanup()
