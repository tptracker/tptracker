# This is the code for connecting excel to python
from typing import Dict, List

# This is the code for connecting to the serial port of Arduino.
# adaped from https://www.learnrobotics.org/blog/arduino-data-logger-csv/'s version
import serial

arduino_port = "COM5" #serial port of Arduino
baud = 9600 #arduino uno runs at 9600 baud
fileName="Output_CSV_from_Arduino.csv" #name of the CSV file generated

# the interval after which we have to check the changes in the .csv file
CHECK_INTERVAL = 10


# dumper: a bathroom user
# dumpstation : a bathroom
#
# HIGHLIGHTS:
#
# 1. The program will be running continuously as it will have to read the 
#    changing csv file. 
# 
# 2. We can check for data after every 10 minutes. 
#    I thought of 10 minutes because I assumed that will be the average interval 
#    between two dumpers will visiting a specific dumpstation. We may change 
#    this value in future
#
# 3. After a check if False is detected in a room, we will want to email the 
#    staff. 
#

def data_extractor(file) -> Dict[str, bool]:
    """ Reads the data from the <file> and -+returns a dict with keys as the
    location and value as the current status of the toilet paper.

    --- Significance of Values ---
    True:
        Toilet paper is present
    False:
        Toilet paper is empty and needs a refill"""
    # TODO: Implement this function
    
    # This sets up the serial connection and creates the file.
    ser = serial.Serial(arduino_port, baud)
    print("Connected to Arduino port:" + arduino_port)
    file = open(fileName, "w")
    print("Created file")
    
    #display the data to the terminal
    getData=str(ser.readline())
    data=getData[0:][:-2]
    print(data)

    #add the data to the file
    file = open(fileName, "a") #append the data to the file
    file.write(data + "\\n") #write data with a newline

    #close out the file
    file.close()


# TODO: Create a function to automate data check after every <CHECK_INTERVAL> 
#  minutes


def data_scanner(info: Dict[str, bool]):  # return type to be assigned
    """ Scans through the <info> and detects if a False value exists triggers
    the email function"""
    # TODO: Implement this function

# TODO: Create a function to send email as <data_scanner> triggers it to
