# This is the code for connecting excel to python
from typing import Dict, List
from time import sleep
# Code for sending emails
import smtplib,ssl
from email.message import EmailMessage
from email.headerregistry import Address
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


def data_updater() -> None:
    """ Checks for data after every <CHECK_INTERVAL> minutes"""
    full = True
    # while every toilet paper is full
    while full:
        file = open('test_data.csv', 'r')
        data = data_extractor(file)
        # Checking if there is a toilet roll which is empty
        for room, status in data.items():
            if not status:
                send_email(room)
        # Recheck for data after 10 minutes
        sleep(CHECK_INTERVAL * 60)


def send_email(location: str) -> None:
    """ Sends an email to the manager informing him about the location of the toilet where
    toilet roll has exhausted """
    email = EmailMessage()
    email['Subject'] = "Defiency in Toilet Paper at " + location

    # Using Address Class to set misaddresses
    email['From'] = Address("TP Tracker", "tpdeficiencyalert",
                            "gmail.com")  # tpdeficiencyalert@gmail.com
    email['To'] = Address("", "mahithedula",
                          "gmail.com")  # change to cleanit@andrew.cmu.edu

    # Creating the Body of the Email
    message = " Greetings, There is a deficiency in toilet paper at " + \
              location + ". Hopefully you can fix it. Thanks, TP Tracker"
    email.set_content(message)

    # Sending email message
    secure = ssl.create_default_context()
    try:
        with smtplib.SMTP("smtp.gmail.com", 465, secure) as server:
            server.login("tpdeficiencyalert@gmail.com",
                         "NewbieHacks")  # username and password
            server.send_message(email)
        print("Successfully sent")
    except Exception as error:
        print("Unsuccessful email")
        print(error)



if __name__ == '__main__':
    input('Press enter to start the searching')
    data_updater()
    # TODO: type 'exit' to stop the program
