#include <LiquidCrystal.h> // include library of LCD
LiquidCrystal lcd(13, 12, 11, 10, 9,
                 8);    // attach LCD pin RS,E,D4,D5,D6,D7 to the given pins
int LDR_sensor_Pin = A0; // select the input pin for the potentiometer
int LDR_sensor_ADC_Value =
    0;           // variable to store the value coming from the sensor
int RED_LED = 7; // assign pin 7 to RED_LED
void setup() {
    lcd.begin(20, 4);                  // Initialise 20*4 LCD
    pinMode(RED_LED, OUTPUT);          // use RED_LED as an output
    lcd.setCursor(0, 0);               // set cursor of LCD at column0 and Row0
    lcd.print("LDR based light");      // print string on LCD
    lcd.setCursor(0, 1);               // set cursor on LCD
    lcd.print("intensity monitoring"); // print string on LCD
    lcd.setCursor(0, 2);               // set cursor on LCD
    lcd.print("system at LPU");        // print string on LCD
    delay(1000);                       // delay of 1000 mS
    lcd.clear();                       // clear the contents of LCD
}
void loop() {
    LDR_sensor_ADC_Value = analogRead(LDR_sensor_Pin); // read the
    value from the sensor lcd.setCursor(0, 2);         // set cursor on LCD
    lcd.print("ADC LEVEL+LDR:");                       // print string on LCD
    lcd.setCursor(17, 2);                              // set cursor on LCD
    lcd.print(LDR_sensor_ADC_Value);                   // // print value on LCD
    if (LDR_sensor_ADC_Value >= 100) {
        digitalWrite(RED_LED, HIGH); // make pin7 to HIGH
        delay(20);                   // delay of 20 mS
    } else {
        digitalWrite(RED_LED, LOW); // make pin7 to HIGH
        delay(20);                  // delay of 20 mS
    }
}
