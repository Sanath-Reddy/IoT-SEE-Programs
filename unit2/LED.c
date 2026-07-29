int LED_CONTROL = 4;

void setup()
{
    pinMode(LED_CONTROL, OUTPUT);  // initialize pin 4 as output pin
}

void loop()
{
    digitalWrite(LED_CONTROL, HIGH);  // Make pin 4 HIGH
    delay(1000);                      // 1000 mS delay

    digitalWrite(LED_CONTROL, LOW);   // Make pin 4 HIGH
    delay(1000);                      // 1000 mS delay
}