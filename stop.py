import sys, os, netifaces, psutil, board, adafruit_ssd1306, time
from PIL import Image, ImageDraw, ImageFont

def main():
    #Define some constants and variables
    WIDTH = 128
    HEIGHT = 32  # Change to 64 if needed
    BORDER = 5
    ADDRESS= 0x3C

    #Init the display
    i2c=board.I2C()
    oled=adafruit_ssd1306.SSD1306_I2C( WIDTH, HEIGHT, i2c, addr=ADDRESS )
    oled.fill( 0 )
    oled.show()

if __name__ == "__main__":
    main()
