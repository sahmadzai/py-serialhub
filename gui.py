# gui.py
#
# Author: Shamsullah Ahmadzai & Sohan Sunku
# Date: 2023-07-15
# Version: 0.0.1
# Description: GUI file for the serial hub CLI application that will be run on a Raspberry Pi. Returns the GUI to main.py
#
#!/bin/bash

# Importing the necessary libraries
import termcolor
from tabulate import tabulate

# title()
# Prints the title for the GUI to the console to say "SerialHub" in ASCII art
# Parameters: None
def title():
    # Printing the GUI to the console to say "SerialHub" in ASCII art
    print(termcolor.colored("=============================================================", "green"))
    print(termcolor.colored("   _____              _         _  _   _         _     ", "green"))
    print(termcolor.colored("  /  ___|            (_)       | || | | |       | |    ", "green"))
    print(termcolor.colored("  \ `--.   ___  _ __  _   __ _ | || |_| | _   _ | |__  ", "green"))
    print(termcolor.colored("   `--. \ / _ \| '__|| | / _` || ||  _  || | | || '_ \ ", "green"))
    print(termcolor.colored("  /\__/ /|  __/| |   | || (_| || || | | || |_| || |_) |", "green"))
    print(termcolor.colored("  \____/  \___||_|   |_| \__,_||_|\_| |_/ \__,_||_.__/ ", "green"))
    print(termcolor.colored("                                                       ", "green"))
    print(termcolor.colored("                                                       ", "green"))
    print(termcolor.colored("=============================================================", "green"))


# printserial()
# Prints the serial connections information
# Parameters: None
def printserial(serial_info):
    # Creating a table of serial information
    table_headers = ["Port", "Description", "Hardware ID"]
    table_data = [(port, desc, hwid) for port, desc, hwid in serial_info]
    table = tabulate(table_data, headers=table_headers, tablefmt="grid")
    
    # Printing the serial information table
    print(table)




    