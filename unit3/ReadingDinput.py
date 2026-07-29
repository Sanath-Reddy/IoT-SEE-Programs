import RPi.GPIO as GPIO

# Use Raspberry Pi in BCM mode
GPIO.setmode(GPIO.BCM)

# Set GPIO 23 as input with pull-down resistor
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set GPIO 24 as input with pull-up resistor
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(23) == 1:
        print("Pressed Button 1")

    if GPIO.input(24) == 0:
        print("Pressed Button 2")

# Clean up all GPIOs
GPIO.cleanup()