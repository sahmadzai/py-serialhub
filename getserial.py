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

def getserial():
    # Getting the serial connections information (identifiers, port, protocol, etc.) from the Raspberry Pi
    ports = serial.tools.list_ports.comports()

    # Returning the serial connections information (identifiers, port, protocol, etc.) from the Raspberry Pi to main.py
    return ports

# printserial()
# Prints the serial connections information
# Parameters: None
def printserial(serial_info):
    # Creating a table of serial information
    table_headers = ["Port", "Description", "Hardware ID"]
    table_data = []
    
    for port, desc, hwid in serial_info:
        if port == "/dev/serial0":
            port = "/dev/ttyS0"  # Map /dev/serial0 to /dev/ttyS0
        table_data.append((port, desc, hwid))
    
    table = tabulate(table_data, headers=table_headers, tablefmt="grid")
    
    # Printing the serial information table
    print(table)

