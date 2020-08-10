# Raspberry PI Distance Calculator

## Introduction
Raspberry PI distance calculator is a simple PI project which can be used to measure distance between two points and forward the events to Splunk for further analysis. 
It uses GPIO modules to trigger an ultrasonic sensor and calculate the difference in time between send and recieve timestamps.

Following acronyms will be used from here onwards
RPI = Raspberry PI
GPIO = general-purpose input/output

## Components

RPI Distance Calculator used low cost electronic components and are listed 

1. HC-SR04 Ultrasonic Sensor
2. Resistor : 330Ω
3. Resistor : 470Ω 

## Circuit Diagram and Connections

Connections from the sensors are as below

* VCC -> Pin  2 of RPI
* GND -> Pin  6 of RPI 
* TRIG -> Pin 12 of RPI
* ECHO -> Pin 18 of RPI through 330Ω Resistor
* 330Ω -> Pin  6 of RPI through 470Ω Resistor

![rpi_distance_cal_circuit_diagram](https://github.com/rcpnair/rpi_distance_calc/blob/master/rpi_distance_cal_circuit_diagram.jpg)



