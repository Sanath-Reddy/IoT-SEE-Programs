import I2C_LCD_driver
import time

# Initialize the I2C LCD
mylcd = I2C_LCD_driver.lcd()

while True:
    # Display current time on the first row
    mylcd.lcd_display_string(
        "Time: %s" % time.strftime("%H:%M:%S"), 1
    )

    # Display current date on the second row
    mylcd.lcd_display_string(
        "Date: %s" % time.strftime("%m/%d/%Y"), 2
    )

    # Update every second
    time.sleep(1)