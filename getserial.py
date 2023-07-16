# getserial.py
#
# Author: Shamsullah Ahmadzai & Sohan Sunku
# Date: 2023-07-15
# Version: 0.0.1
# Description: Gets the serial connections information (identifiers, port, protocol, etc.) from the Raspberry Pi and returns it to main.py
#
#!/bin/bash

# Importing the necessary libraries

import glob
import os
import re
from datetime import datetime
from tabulate import tabulate

def getserial():
    # Retrieve the list of active serial ports
    port_paths = glob.glob('/dev/serial*')
    
    # Extract the port, permissions, date, path, and target information
    table_data = []
    for port_path in port_paths:
        port = port_path
        permissions = ""
        date = ""
        target = ""
        
        # Get the symbolic link information
        if os.path.islink(port_path):
            link_path = os.path.realpath(port_path)
            permissions = get_permissions(port_path)
            date = get_date(port_path)
            target = os.path.basename(link_path)
        
        table_data.append((port, decode_permissions(permissions), date, target))
    
    # Returning the serial connections information (port, permissions, date, path, target) from the Raspberry Pi to main.py
    return table_data

def get_permissions(path):
    # Retrieve the permissions of the specified path
    return oct(os.stat(path).st_mode)[-3:]

def decode_permissions(permissions):
    # Decode the permissions into text format
    permission_codes = {
        "0": "---",
        "1": "--x",
        "2": "-w-",
        "3": "-wx",
        "4": "r--",
        "5": "r-x",
        "6": "rw-",
        "7": "rwx",
    }

    user_permissions = permission_codes.get(permissions[0], "???")
    group_permissions = permission_codes.get(permissions[1], "???")
    other_permissions = permission_codes.get(permissions[2], "???")

    return f"U: {user_permissions}  |  G: {group_permissions}  |  O: {other_permissions}"

def get_date(path):
    # Retrieve the date of creation/modification of the specified path
    timestamp = os.path.getctime(path)
    return format_date(timestamp)

def format_date(timestamp):
    # Format the timestamp into a readable date format
    date_time = datetime.fromtimestamp(timestamp)
    formatted_date = date_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date
