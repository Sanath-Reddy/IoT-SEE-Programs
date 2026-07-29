import I2C_LCD_driver
import socket
import fcntl
import struct

# Initialize the I2C LCD
mylcd = I2C_LCD_driver.lcd()

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    return socket.inet_ntoa(
        fcntl.ioctl(
            s.fileno(),
            0x8915,                          # SIOCGIFADDR
            struct.pack('256s', ifname[:15].encode('utf-8'))
        )[20:24]
    )

# Display IP address on LCD
mylcd.lcd_display_string("IP Address:", 1)
mylcd.lcd_display_string(get_ip_address('wlan0'), 2)