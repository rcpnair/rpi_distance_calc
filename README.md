# Raspberry PI Distance Calculator
## Table of Contents
* [Introduction](#introduction)
* [Components](#components)
  * [Hardware Components](#hardware-components)
  * [Software Components](#software-components)
* [Circuit Diagram](#circuit-diagram)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Use case 1 - Connected furniture](#use-case-1---connected-furniture)
* [License](#license)
* [Acknowledgements](#acknowledgements)

## Introduction
<p>
Raspberry PI distance calculator is a simple python project that can be used to measure distance between two points and forward the events to Splunk for further analysis. 
</p>

It uses [GPIO](https://www.raspberrypi.org/documentation/usage/gpio/) modules of Raspberry PI to trigger an ultrasonic sensor and calculate the difference between send and recieve timestamps.

**Ultra Sonic Sensor**

<p>
 
An *ultrasonic sensor* is an electronic device that measures the distance of a target object by emitting ultrasonic sound waves, and converts the reflected sound into an electrical signal.

In order to calculate the distance between the sensor and the object, the sensor measures the time it takes between the emission of the sound by the transmitter to its contact with the receiver. 
</p>
<p>
 The formula for this calculation is D = ½ T x C (where D is the distance, T is the time, and C is the speed of sound ~ 343 meters/second).
</p>
Following acronyms will be used from here onwards

* RPI = Raspberry PI
* GPIO = general-purpose input/output

## Components

### Hardware Components

1. Raspberry PI (3 & 4 tested)
2. HC-SR04 Ultrasonic Sensor
3. Resistor : 330Ω
4. Resistor : 470Ω 

### Software Components

* Python
* Splunk

## Circuit Diagram

Connections from the sensor and components are as below.

For detailed information about the GPIO Pins and description, please check [GPIO](https://www.raspberrypi.org/documentation/usage/gpio/)

* VCC -> Pin  2 of RPI
* GND -> Pin  6 of RPI 
* TRIG -> Pin 12 of RPI
* ECHO -> Pin 18 of RPI through 330Ω Resistor
* 330Ω -> Pin  6 of RPI through 470Ω Resistor


![rpi_distance_cal_circuit_diagram](https://github.com/rcpnair/rpi_distance_calc/blob/master/images/rpi_distance_cal_circuit_diagram.jpg)
## Getting Started

Follow the steps to configure and start the project.

### Prerequisites

RPI Distance Calculator uses Splunk HTTP Collector to send data data to Splunk and then to analyse and visualize data. 

Follow the [Splunk HEC Documentation](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector) to set up Splunk HTTP Event Collector.

If Splunk set up is not available , you may switch off Splunk connections by setting following configuration in [config.ini](https://github.com/rcpnair/rpi_distance_calc/blob/master/config.ini)

```
[ splunk ]
disable = True
```

### Installation

1. Install Python3
2. Intall the dependencies
    ```
    pip3 install configparser
    pip3 install argparse
    pip3 install git+git://github.com/georgestarcher/Splunk-Class-httpevent.git
    ```
3. Clone or download the repo to raspberry PI
    ```
    git clone https://github.com/rcpnair/rpi_distance_calc.git
    ```
4. Configure [config.ini](https://github.com/rcpnair/rpi_distance_calc/blob/master/config.ini)

5. Run the distance.py
Add execution permission to the file and run
`./distance.py`

# Usage
Program uses config.ini configuration file to get all required parameters.
<p>
If any of the parameters are not available, it uses the default values
</p>
<p>
By default, it looks in the current working directory of the program for config.ini file
 </p>
<p>
You may override it and supply config from other locations using _--config_ or _-c_ parametert from the command line.
 </p>
 
`./distance.py --config /path/to/config_file_in_ini_format/`
# Use case 1 - Connected furniture
<p>
 Using the distance calculator, height of an adjustable table can be measured and send data to splunk for further analysis.
 
 ## Sample Dashboards
 
![splunk_dashboard_amber](https://github.com/rcpnair/rpi_distance_calc/blob/master/images/splunk_dashboard_amber.jpg)

![splunk_dashboard_red](https://github.com/rcpnair/rpi_distance_calc/blob/master/images/splunk_dashboard_red.jpg)


# License
Distributed under the MIT License. See LICENSE for more information.

# Acknowledgements
Thanks to [georgestarcher](https://github.com/georgestarcher) for an awesome and easy to use Python Class for [ Splunk HEC ](https://github.com/georgestarcher/Splunk-Class-httpevent)
