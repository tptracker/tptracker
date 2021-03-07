# This is the code for connecting excel to python
# Code for sending emails
import smtplib
import ssl
from datetime import datetime
from email.headerregistry import Address
from email.message import EmailMessage
from time import sleep
from typing import Dict

# This is the code for connecting to the serial port of Arduino. adapted from
# https://www.learnrobotics.org/blog/arduino-data-logger-csv/'s version
import serial

arduino_port = "COM3"  # serial port of Arduino
baud = 9600  # arduino uno runs at 9600 baud
FILE_NAME = "Output_CSV_from_Arduino.csv"  # name of the CSV file generated

# the interval after which we have to check the changes in the .csv file
CHECK_INTERVAL = .1


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


def data_extractor_and_updater(filename) -> str:
    """ Reads the data from the <file> and -+returns a dict with keys as the
    location and value as the current status of the toilet paper.

    --- Significance of Values ---
    True:
        Toilet paper is present
    False:
        Toilet paper is empty and needs a refill

    Precondition: Every room has a different name"""
    alert = True
    active = True
    while active:
        # opens the file
        opened = open(filename, 'r')
        # reading the column headers
        line = opened.readline()
        if line == '0\n' or line =='0':
            alert = False
        # for every line in file
        while line:
            if not alert:
                # datetime object containing current date and time
                now = datetime.now()
                # convert into str
                dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
                send_email(NAME, dt_string)
                return 'Done'
            # read the next line
            line = opened.readline()
            if line == '0\n' or line == '0':
                alert = False
            # Recheck for data after 10 minute
        sleep(CHECK_INTERVAL * 60)
        print('rechecking')


def create_data_file() -> None:
    """ Creates the data file"""
    # This sets up the serial connection and creates the file.
    ser = serial.Serial(arduino_port, baud)
    print("Connected to Arduino port:" + arduino_port)
    file = open(FILE_NAME, "a")
    print("Created file")

    active = True
    while active:
        # display the data to the terminal
        get_data = str(ser.readline())
        data = get_data[2:][:-5]
        print(data)

        # add the data to the file
        file = open(FILE_NAME, "a")  # append the data to the file
        file.write(data + "\n")  # write data with a newline
        if data[-5:] == "False":
            active = False
    # i.e. once the toilet roll is empty it will close the file
    file.close()


def send_email(location: str, date: str) -> None:
    email = EmailMessage()
    email['Subject'] = "Toilet Paper Replacement at " + location

    name = input('Enter the First and Last name of the reciever')
    username = input('Enter the receiver username (first part of the address before the @)')
    domain = input('Enter the domain of the receiver (ex: gmail.com)')
    
    #Using Address Class to set emailaddresses
    email['From'] = Address("TP Tracker", "tpdeficiencyalert", "gmail.com" ) #tpdeficiencyalert@gmail.com
    email['To'] = Address(name, username, domain)

    # Creating the Body of the Email
    message = f""" 
    Greetings,  
    
    As of {date}, the toilet paper in {location} ran out.
    Hopefully you can replace it. 
    
    Thanks, 
    TP Tracker
    
    """
    email.set_content(message)

    # Sending email message
    secure = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=secure) as server:
            server.login("tpdeficiencyalert@gmail.com",
                         "NewbieHacks")  # username and password
            server.send_message(email)
        print("Successfully sent")
    except Exception as error:
        print("Unsuccessful email")
        print(error)


if __name__ == '__main__':
    call = True
    while call:
        print('Beginning setup')
        NAME = input("Name of the room")
        input('Press enter to start the searching')
        # creates the data file
        create_data_file()
        data_extractor_and_updater(FILE_NAME)
        ask = input("Do you want to restart? (y/n)")
        if ask == 'n':
            call = False

