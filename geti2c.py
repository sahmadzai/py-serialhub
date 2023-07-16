# geti2c.py
#
# Author: Shamsullah Ahmadzai & Sohan Sunku
# Date: 2023-07-15
# Version: 0.0.1
# Description: Gets the serial connections information (identifiers, port, protocol, etc.) from the Raspberry Pi and returns it to main.py
#
#!/bin/bash

# Importing the necessary libraries
import smbus2

def geti2c():
    # Open the I2C bus
    bus = smbus2.SMBus(1)  # Use the appropriate bus number (0 or 1) for your Raspberry Pi

    # List to store the detected device addresses
    detected_devices = []

    # Iterate over possible device addresses
    for address in range(0, 128):
        try:
            # Check if the device at the address acknowledges
            bus.read_byte(address)
            detected_devices.append(hex(address))

        except smbus2.SMBusError:
            pass

    # Print the detected device addresses
    print("Detected I2C Devices:")

    return detected_devices
