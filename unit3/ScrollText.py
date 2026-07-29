import I2C_LCD_driver
from time import sleep

# Initialize the I2C LCD
mylcd = I2C_LCD_driver.lcd()

# Create 16 blank spaces for padding
str_pad = " " * 16

# Message to scroll
my_long_string = "This is a string that needs to scroll"

# Add padding to the beginning of the message
my_long_string = str_pad + my_long_string

while True:
    for i in range(0, len(my_long_string)):
        # Display a 16-character window of the message
        lcd_text = my_long_string[i:i + 16]

        mylcd.lcd_display_string(lcd_text, 1)

        # Scroll speed
        sleep(0.4)

        # Clear the first line
        mylcd.lcd_display_string(str_pad, 1)