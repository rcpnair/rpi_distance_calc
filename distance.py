#!/usr/bin/python3
import os
import sys
import logging
import time
from argparse import ArgumentParser
import rpi as RPI
import config
import splunk_hec as splunk

# Define splunk related config and get a connection to splunk HEC


def getSplunkConn():

    disable = config.getVal("splunk", "disable", False, True)
    if disable:
        log.warning(
            "Splunk is disabled in the config, events will not be forwarded")
        return None, None

    host = config.getVal("splunk", "host", "localhost")
    port = config.getVal("splunk", "port", "8088")
    token = config.getVal("splunk", "token", "HTTP-EVENT-COLLECTOR-TOKEN")
    secure = config.getVal("splunk", "secure_host", False, True)  # http/https

    index = config.getVal("splunk", "index", "main")
    source = config.getVal("splunk", "source", "raspberry")
    sourcetype = config.getVal("splunk", "sourcetype", "_json")

    event_format = config.getVal("splunk", "event_format", "json")
    event_host = config.getVal("splunk", "event_host", "raspberry")

    hecConn = splunk.getHecConn(
        token,
        host,
        event_format,
        event_host,
        port,
        secure)

    # initialize a payload which will be used later to send event
    payLoad = splunk.initSplunkPayload(index, host, source, sourcetype)

    return hecConn, payLoad


# Set the logging parameters
# Log level can be set in config
logging.basicConfig(
    format='%(asctime)s %(name)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %z',
    level=logging.DEBUG)
log = logging.getLogger(name="main")

log.info("Initializing ...")
# Default config file is set in case configuration is not passed
# External config can be passed using -c
pwd = os.getcwd()
fName = "config.ini"

localConf = os.path.join(pwd, fName)

# Read and process args from command line
# If no config file provided, default one will be picked up
parser = ArgumentParser()
parser.add_argument(
    "-c",
    "--config",
    dest="confFile",
    default=localConf,
    help="Config file")

args = parser.parse_args()

if not os.path.isfile(args.confFile):
    log.critical("Config file %s not found, exiting", args.confFile)
    sys.exit(1)

log.info("Using configuration file %s", args.confFile)

config.readConf(args.confFile)

log.setLevel(config.getVal("log", "level", "INFO"))

signalTimeout = config.getVal("rpi", "signal_timeout", 3)
interval = config.getVal("rpi", "interval", 1)
doSplunk = True

# Connect to Splunk HTTP event collector
hec, payload = getSplunkConn()

if hec is None:
    log.error(
        "Unable to get connection to Splunk HTTP Event Collector. Events will not be forwarded")
    doSplunk = False

else:
    hec.popNullFields = True
    # set logging to DEBUG for example
    hec.log.setLevel(config.getVal("log", "level", "INFO"))

# main

if __name__ == '__main__':

    try:
        log.info("Initilizing PI configurations")
        RPI.initPI()

        # Run a continous loop to calculate difference and send output
        while True:
            log.info("Triggering the signal and calculating the distance")
            distance = RPI.getDistance(signalTimeout)

            if distance < 0:
                log.error(
                    "Signal timed out after waiting for %d seconds at %d. Check your circuit/connections",
                    signalTimeout,
                    distance)
                RPI.cleanup()
                sys.exit(2)

            log.info("Distance is %d ", distance)

            # Send to splunk only if splunk is enabled and a successful splunk connection , print
            # on the console otherwise
            if doSplunk:
                payload.update({"event": {"distance": distance}})
                eventTime = time.time()
                hec.sendEvent(payload, eventTime)

            time.sleep(interval)

    #CTRL + C
    except KeyboardInterrupt:
        log.info("Keyboard interrupt received from user. Exiting")
        RPI.cleanup()
