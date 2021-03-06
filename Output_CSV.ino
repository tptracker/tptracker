/*
  Button

  Turns on and off a light emitting diode(LED) connected to digital pin 13,
  when pressing a pushbutton attached to pin 2.

  The circuit:
  - LED attached from pin 13 to ground
  - pushbutton attached to pin 2 from +5V
  - 10K resistor attached to pin 2 from ground

  - Note: on most Arduinos there is already an LED on the board
    attached to pin 13.

  created 2005
  by DojoDave <http://www.0j0.org>
  modified 30 Aug 2011
  by Tom Igoe

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/Button

  Used https://www.learnrobotics.org/blog/arduino-data-logger-csv/ to help with outputting a CSV file.
*/

// constants won't change. They're used here to set pin numbers:
const int buttonPin = 3;     // the number of the pushbutton pin
const int ledPin =  11;      // the number of the LED pin
int currMode = LOW;    // this keeps track of whether the past button read was on/off
String bathroomLabel = "Room1";
bool label = true;

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  //print out column headers
  while(label) { //runs once
    Serial.println(bathroomLabel);
    label = false;
  }
  
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);
  
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState != currMode) {
    //set the current equal to the data
    currMode = buttonState;
    digitalWrite(ledPin, buttonState);
    
    // Display Data to Cerial Monitor
    Serial.println(buttonState);
    Serial.print(",");
    if (buttonState == HIGH) {
      Serial.println("True");
    }
    else {
      Serial.println("False");
    }
    
  }
  delay(500);
}
