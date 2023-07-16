# gpio_info.py
#
# Author: Shamsullah Ahmadzai & Sohan Sunku
# Date: 2023-07-15
# Version: 0.0.1
# Description: Gets the GPIO pin information (pin number, function, hardware ID, etc.) from the Raspberry Pi and returns it to main.py
#
#!/bin/bash

from tabulate import tabulate
import subprocess

# Define the I2C and UART ports
i2c_port = "/dev/i2c-1"  # Modify according to your specific I2C port
uart_port = "/dev/serial0"  # Modify according to your specific UART port

# Execute the gpio command to retrieve pin mappings
i2c_pin_info = subprocess.check_output(["gpio", "-g", "readall", i2c_port]).decode("utf-8")
uart_pin_info = subprocess.check_output(["gpio", "-g", "readall", uart_port]).decode("utf-8")

# Parse the gpio command output to extract pin information
def parse_pin_info(pin_info):
    lines = pin_info.strip().split("\n")
    table_data = []
    for line in lines[3:-1]:
        parts = line.split("|")
        pin_num = parts[1].strip()
        pin_func = parts[3].strip()
        pin_hardware_id = parts[4].strip()
        table_data.append((pin_num, pin_func, pin_hardware_id))
    return table_data

# Format and print the GPIO pin information in a table
table_headers = ["Pin", "Function", "Hardware ID"]
i2c_table_data = parse_pin_info(i2c_pin_info)
uart_table_data = parse_pin_info(uart_pin_info)
table_data = i2c_table_data + uart_table_data

print(tabulate(table_data, headers=table_headers, tablefmt="grid"))
