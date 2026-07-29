from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
from signal import pause

# Create objects for PIR motion sensor and Pi Camera
pir = MotionSensor(4)      # PIR sensor connected to GPIO 4
camera = PiCamera()

# Start the camera
camera.rotation = 180
camera.start_preview()

# Image counter
i = 0

# Function to capture an image when motion is detected
def take_photo():
    global i
    i += 1
    camera.capture('/home/pi/Images/image_%s.jpg' % i)
    print("A photo has been taken")
    sleep(10)   # Wait 10 seconds before detecting another motion

# Capture photo when motion is detected
pir.when_motion = take_photo

# Keep the program running
pause()