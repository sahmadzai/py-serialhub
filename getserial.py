# getserial.py
#
# Author: Shamsullah Ahmadzai & Sohan Sunku
# Date: 2023-07-15
# Version: 0.0.1
# Description: Gets the serial connections information (identifiers, port, protocol, etc.) from the Raspberry Pi and returns it to main.py
#
#!/bin/bash

# Importing the necessary libraries
import serial.tools.list_ports

# getserial()
# Gets the serial connections information (identifiers, port, protocol, etc.) from the Raspberry Pi
# Parameters: None
def getserial():
    # Getting the serial connections information (identifiers, port, protocol, etc.) from the Raspberry Pi
    ports = serial.tools.list_ports.comports()

    # Returning the serial connections information (identifiers, port, protocol, etc.) from the Raspberry Pi to main.py
    return ports
