// Motor Driver Pins (Channel A)
int directionPin = 12;
int pwmPin = 3;
int brakePin = 9;

// Uncomment these if using Channel B
// int directionPin = 13;
// int pwmPin = 11;
// int brakePin = 8;

// Boolean to switch motor direction
bool directionState = false;

void setup() {
  // Define pins as outputs
  pinMode(directionPin, OUTPUT);
  pinMode(pwmPin, OUTPUT);
  pinMode(brakePin, OUTPUT);
}

void loop() {

  // Toggle direction each loop
  directionState = !directionState;

  // Set motor direction
  if (directionState == false) {
    digitalWrite(directionPin, LOW);
  } else {
    digitalWrite(directionPin, HIGH);
  }

  // Release brake
  digitalWrite(brakePin, LOW);

  // Run motor at low speed (PWM = 30)
  analogWrite(pwmPin, 30);

  // Run for 2 seconds
  delay(2000);

  // Apply brake
  digitalWrite(brakePin, HIGH);

  // Stop motor
  analogWrite(pwmPin, 0);

  // Wait for 2 seconds
  delay(2000);
}