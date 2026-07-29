#include <LiquidCrystal.h> // include library of LCD
LiquidCrystallcd(13, 12, 11, 10, 9, 8); // attach LCD pin RS, E, D4, D5, D6, D7 to the given pins

int MPIN1 = 7;  // assign pin 7 as MPIN1
int MPIN2 = 6;  // assign pin 6 as MPIN2
int MPIN3 = 5;  // assign pin 5 as MPIN3
int MPIN4 = 4;  // assign pin 4 as MPIN4

void setup()
{
    pinMode(MPIN1, OUTPUT);  // make MPIN1 as an output
    pinMode(MPIN2, OUTPUT);  // make MPIN2 as an output
    pinMode(MPIN3, OUTPUT);  // make MPIN3 as an output
    pinMode(MPIN4, OUTPUT);  // make MPIN4 as an output

    lcd.begin(20, 4);  // initialise LCD
    lcd.setCursor(0, 0);  // set cursor on LCD
    lcd.print("DC Motor direction");  // print string on LCD
    lcd.setCursor(0, 1);  // set cursor on LCD
    lcd.print("control system...");  // print string on LCD
    delay(1000);  // delay of 1000 mS
    lcd.clear();  // clear the contents of LCD
}

void loop()  // infinite loop
{
    digitalWrite(MPIN1, HIGH);  // make MPIN1 to HIGH
    digitalWrite(MPIN2, LOW);  // make MPIN2 to LOW
    digitalWrite(MPIN3, HIGH);  // make MPIN3 to HIGH
    digitalWrite(MPIN4, LOW);  // make MPIN4 to LOW

    lcd.setCursor(0, 2);  // set cursor on LCD
    lcd.print("CLOCKWISE");  // print string on LCD
    delay(2000);  // delay of 2 sec
    lcd.clear();  // clear the contents of LCD

    digitalWrite(MPIN1, LOW);  // make MPIN1 to LOW
    digitalWrite(MPIN2, HIGH);  // make MPIN2 to HIGH
    digitalWrite(MPIN3, LOW);  // make MPIN3 to LOW
    digitalWrite(MPIN4, HIGH);  // make MPIN4 to HIGH

    lcd.setCursor(0, 2);  // set cursor on LCD
    lcd.print("ANTI-CLOCKWISE");  // print string on LCD
    delay(2000);  // delay of 2 Sec
    lcd.clear();  // clear the contents of LCD

    digitalWrite(MPIN1, LOW);  // make MPIN1 to LOW
    digitalWrite(MPIN2, LOW);  // make MPIN2 to LOW
    digitalWrite(MPIN3, HIGH);  // make MPIN3 to HIGH
    digitalWrite(MPIN4, LOW);  // make MPIN4 to LOW

    lcd.setCursor(0, 2);  // set cursor on LCD
    lcd.print("LEFT");  // print string on LCD
    delay(2000);  // delay of 2 Sec
    lcd.clear();  // clear the contents of LCD

    digitalWrite(MPIN1, HIGH);  // make MPIN1 to HIGH
    digitalWrite(MPIN2, LOW);  // make MPIN2 to LOW
    digitalWrite(MPIN3, LOW);  // make MPIN3 to LOW
    digitalWrite(MPIN4, LOW);  // make MPIN4 to LOW

    lcd.setCursor(0, 2);  // set cursor on LCD
    lcd.print("RIGHT");  // print string on LCD
    delay(2000);  // delay of 2 Sec
    lcd.clear();  // clear the contents of LCD
}