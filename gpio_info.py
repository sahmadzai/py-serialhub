# gpio_info.py
#
# Author: Shamsullah Ahmadzai & Sohan Sunku
# Date: 2023-07-15
# Version: 0.0.1
# Description: Gets the GPIO pin information (pin number, function, hardware ID, etc.) from the Raspberry Pi and returns it to main.py
#
#!/bin/bash

from gpiozero import GPIODevice, Pin
from tabulate import tabulate

# Define the I2C and UART pin numbers
i2c_pins = [2, 3]  # Modify according to your specific GPIO pin numbers for I2C
uart_pins = [14, 15]  # Modify according to your specific GPIO pin numbers for UART

# Get detailed information for I2C pins
i2c_pin_info = [Pin(pin) for pin in i2c_pins]
i2c_pin_descriptions = [pin.function for pin in i2c_pin_info]
i2c_pin_hardware_ids = [pin.humanize() for pin in i2c_pin_info]

# Get detailed information for UART pins
uart_pin_info = [Pin(pin) for pin in uart_pins]
uart_pin_descriptions = [pin.function for pin in uart_pin_info]
uart_pin_hardware_ids = [pin.humanize() for pin in uart_pin_info]

# Display the GPIO pin information in a table format
table_headers = ["Pin", "Function", "Hardware ID"]
table_data = list(zip(i2c_pins + uart_pins, i2c_pin_descriptions + uart_pin_descriptions, i2c_pin_hardware_ids + uart_pin_hardware_ids))

print(tabulate(table_data, headers=table_headers, tablefmt="grid"))
