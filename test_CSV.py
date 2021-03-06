# This is the code for connecting to the serial port of Arduino.
# adaped from https://www.learnrobotics.org/blog/arduino-data-logger-csv/'s version
import serial

arduino_port = "COM5" #serial port of Arduino
baud = 9600 #arduino uno runs at 9600 baud
fileName="Output_CSV_from_Arduino.csv" #name of the CSV file generated

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
