import http.client
import urllib.parse
import time
import RPi.GPIO as GPIO
from gpiozero import DistanceSensor

GPIO.setwarnings(False)

# ThingSpeak API Key
key = "MKQ13DILO94GR23J"

# Initialize the ultrasonic sensor once
ultrasonic = DistanceSensor(echo=17, trigger=4)

def ultra():
    while True:
        distance = ultrasonic.distance  # Distance in metres

        print("Distance: {:.3f} m".format(distance))

        params = urllib.parse.urlencode({
            'field1': distance,
            'key': key
        })

        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"
        }

        conn = http.client.HTTPConnection("api.thingspeak.com:80")

        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()

            print(response.status, response.reason)
            print(response.read().decode())

            conn.close()

        except Exception as e:
            print("Connection failed:", e)

        time.sleep(15)   # ThingSpeak free accounts require at least 15 seconds

if __name__ == "__main__":
    ultra()