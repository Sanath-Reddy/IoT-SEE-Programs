#include <LiquidCrystal.h>                // include library of LCD
LiquidCrystal lcd(13, 12, 11, 10, 9, 8);   // attach LCD pin RS,E,D4,D5,D6,D7 to the given pins
int PIR_SENSOR_LOW = 5;                   // assign pin 5 as PIR_SENSOR_LOW
int RED_LED = 7;                          // assign pin 7 as RED_LED
int BLUE_LED = 6;                         // // assign pin 6 as BLUE_LED
void setup() {
    pinMode(PIR_SENSOR_LOW, INPUT_PULLUP); // configure pin5 as an input and enable the internal pull - up resistor
    pinMode(RED_LED, OUTPUT); // configure pin7 as output
    pinMode(BLUE_LED, OUTPUT);                // configure pin6 as output
    lcd.begin(20, 4);    // set up the LCD's number of columns and rows
    lcd.setCursor(0, 0); // set cursor to column0 and row1
    lcd.print("MOTION SENSOR BASED "); // Print a message to the LCD.
    lcd.setCursor(0, 1);               // set cursor to column0 and row1
    lcd.print("MOTION DETECTION ");    // Print a message to the LCD.
    lcd.setCursor(0, 2);               // set cursor to column0 and row2
    lcd.print("SYSTEM AT LPU");        // Print a message to the LCD.
    delay(1000);
}
void loop() {
    int PIR_SENSOR_LOW_READ = digitalRead(PIR_SENSOR_LOW);
    // read the PIR value into a variable
    if (PIR_SENSOR_LOW_READ == LOW) // Read PIN 5 as LOW PIN
    {
        lcd.clear();                   // clear the contents of the LCD
        lcd.setCursor(0, 3);           // set cursor to column0 and row2
        lcd.print("MOTION DETECTED "); // Print a message to the LCD.
        digitalWrite(RED_LED, HIGH);   // Make pin7 to HIGH
        digitalWrite(BLUE_LED, LOW);   // Make pin6 to LOW
        delay(20);                     // delay of 20 mS
    } else                             // otherwise
    {
        lcd.clear();                       // clear the contents of the LCD
        lcd.setCursor(0, 3);               // set cursor to column0 and row3
        lcd.print("MOTION NOT DETECTED "); // Print a message to the LCD.
        digitalWrite(BLUE_LED, HIGH);      // Make pin 7 to HIGH
        digitalWrite(RED_LED, LOW);        // Low pin6 to LOW
        delay(20);                         // delay of 20 mS
    }
}