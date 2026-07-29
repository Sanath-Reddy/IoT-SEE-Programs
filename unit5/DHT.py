import http.client
import urllib.parse
import time
import RPi.GPIO as GPIO
import Adafruit_DHT

GPIO.setwarnings(False)

key = "TCEHHDU8JBPN2ZNM"

while True:
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)

    print("Temp: {:.1f}C Humidity: {:.1f}%".format(temperature, humidity))

    params = urllib.parse.urlencode({
        'field1': humidity,
        'field2': temperature,
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