#include <LiquidCrystal.h> // include library of LCD
LiquidCrystal lcd(13, 12, 11, 10, 9, 8); // attach LCD pin RS, E, D4, D5, D6, D7
// to the given pins

Servo myservo; // create servo object to control a servo
int POT_PIN = A0; // analog pin used to connect the potentiometer
int POT_PIN_ADC_LEVEL; // variable to read the value from the
// analog pin

void setup()
{
    myservo.attach(3); // attaches the servo on pin 9 to the servo object
    lcd.begin(20, 4); // initialise LCD
    lcd.setCursor(0, 0); // set cursor on LCD
    lcd.print("Servo ANALOG write "); // print string on LCD
    lcd.setCursor(0, 1); // set cursor on LCD
    lcd.print("system at LPU...."); // print string on LCD
}

void loop()
{
    POT_PIN_ADC_LEVEL = analogRead(POT_PIN); // reads POT value
    // in the form of levels
    POT_PIN_ADC_LEVEL = map(POT_PIN_ADC_LEVEL, 0, 1023, 0, 179); // map the value
    // between 0 to 180 degree for servo
    myservo.write(POT_PIN_ADC_LEVEL); // sets the servo position
    // according to the scaled value
    lcd.setCursor(0, 2); // set cursor on LCD
    lcd.print("ANGLE:"); // print string on LCD
    lcd.print(POT_PIN_ADC_LEVEL); // print value on LCD
    delay(15); // delay of 15 mSec
}

