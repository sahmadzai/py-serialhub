# main.py
#
# Author: Shamsullah Ahmadzai & Sohan Sunku
# Date: 2023-07-15
# Version: 0.0.1
# Description: Main file for the serial hub CLI application that will be run on a Raspberry Pi
#
#!/bin/bash

# Importing the necessary libraries and files
import gui
import getserial

# Main function
def main():
    # Print the title
    gui.title()

    # Getting the serial connections information (identifiers, port, protocol, etc.) from the Raspberry Pi and returning it to main.py
    serialinfo = getserial.getserial()

    # Print the serial connections information (identifiers, port, protocol, etc.) from the Raspberry Pi to the console
    gui.printserial(serialinfo)

# Entry point of the program
if __name__ == "__main__":
    main()