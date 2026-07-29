import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Button connected to GPIO 23 with internal pull-up resistor
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LED connected to GPIO 24
GPIO.setup(24, GPIO.OUT)

try:
    while True:
        button_state = GPIO.input(23)

        if button_state == False:
            GPIO.output(24, True)
            print("Button Pressed...")
            time.sleep(0.2)
        else:
            GPIO.output(24, False)

except KeyboardInterrupt:
    GPIO.cleanup()