# Task: Build a Factory Monitoring System

# Your objective is to simulate a factory machine monitoring system using sensor data.
# You will implement a program that uses user inputs to monitor the status of a machine.
# Based on the inputs, your program should evaluate the conditions and print instructions to the user.

# Instructions:

# Step 1: Get User Inputs
# You need to collect three inputs from the user:
# 1. The machine's temperature in degrees Celsius (integer).
# 2. The machine's pressure in PSI (integer).
# 3. The machine's operational status (1 for operating, 0 for stopped) (integer).



# Step 2: Evaluate the Machine's Conditions
# Use conditional statements (if, elif, else) to evaluate the following conditions:

# For temperature:
#  - If the temperature is above 80°C, alert that the temperature is too high and recommend shutting down the machine.
#  - If the temperature is between 50°C and 80°C, indicate that the temperature is within safe limits.
#  - If the temperature is below 50°C, indicate that the machine temperature is low and no action is needed.

# For pressure:
#  - If the pressure exceeds 100 PSI, alert that high pressure is detected and recommend maintenance.
#  - If the pressure is between 70 PSI and 100 PSI, indicate that the pressure is stable.
#  - If the pressure is below 70 PSI, indicate that the pressure is low and the system is operating normally.



# Step 3: Check Operational Status
# Evaluate the machine's operational status:
# - If the machine is operating (1):
#   - If either the temperature is too high or the pressure is too high, alert that the machine is running in unsafe conditions and recommend shutting it down.
#   - If everything is normal, indicate that the machine is running normally.
# - If the machine is not operating (0):
#   - Indicate that the machine is stopped and no immediate action is needed.

# Step 4: Test Your Program
# After completing your program, test it with different inputs to ensure it behaves correctly based on the conditions you implemented.

# ----------------------------------------------------------------------------
# Extension: Log the Results (Note: this requires additional Python knowledge)
# ----------------------------------------------------------------------------

# Create a log file (e.g., "machine_log.txt") to store the results of the evaluation.
# After determining the machine's status, write the following information to the log file:
# - The current temperature, pressure, and operational status.
# - The actions taken based on the evaluations.
# Ensure that each entry in the log file is timestamped to track when the evaluation occurred.
# This extension will help you practice handling file operations in Python.

# Note: Focus on using clear and logical conditional statements to ensure your program functions as expected.
# Remember: when you accept numerical values, you should make sure you consider how robust your code is.
