import time
import I2C_LCD_driver

# Initialize the I2C LCD
mylcd = I2C_LCD_driver.lcd()

while True:
    # Display the message
    mylcd.lcd_display_string("Hello world!")

    # Wait for 1 second
    time.sleep(1)

    # Clear the LCD
    mylcd.lcd_clear()

    # Wait for 1 second
    time.sleep(1)