import time
import board
import adafruit_dht
import thingspeak
from rpi_lcd import LCD

# Define your ThingSpeak channel parameters
channel_id = 2595470
write_key = '86CNU3LZRKBSRJW9'

# Initialize the ThingSpeak channel
channel = thingspeak.Channel(id=channel_id, api_key=write_key)

# Initialize the LCD
lcd = LCD()

# Initialize the DHT11 sensor (connected to GPIO 4)
sensor = adafruit_dht.DHT11(board.D4, use_pulseio=False)

while True:
    try:
        # Read sensor data
        temperature_c = sensor.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = sensor.humidity

        # Print values
        print(
            "Temp={0:0.1f}C, Temp={1:0.1f}F, Humidity={2:0.1f}%".format(
                temperature_c, temperature_f, humidity
            )
        )

        # Display values on LCD
        lcd.text("Temp={}C".format(temperature_c), 1)
        lcd.text("Humi={}%".format(humidity), 2)

        # Send data to ThingSpeak
        response = channel.update({
            'field1': temperature_c,
            'field2': humidity
        })

        print("Data sent to ThingSpeak. Response:", response)

    except RuntimeError as error:
        # DHT sensors often produce temporary read errors
        print(error.args[0])
        time.sleep(2)
        continue

    except Exception as error:
        sensor.exit()
        raise error

    # Wait 15 seconds before the next reading
    time.sleep(15)