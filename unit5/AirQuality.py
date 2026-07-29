import http.client
import urllib.parse
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

key = "HY5941TNS5UP3GZ8"

DO_PIN = 7          # Change if your sensor is connected to another BCM GPIO
GPIO.setup(DO_PIN, GPIO.IN)

def air():
    while True:
        gas_present = GPIO.input(DO_PIN)

        if gas_present == GPIO.LOW:
            gas_state = "Gas Present"
        else:
            gas_state = "No Gas"

        print("Gas State:", gas_state)

        params = urllib.parse.urlencode({
            'field1': gas_present,
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

        time.sleep(15)

if __name__ == "__main__":
    air()