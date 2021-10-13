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
    #Create a bold font (for the IP)
    tmpBoldFont=ImageFont.truetype( '/home/pi/.fonts/lvdcgo.ttf', size=7, index=0, encoding="unic", layout_engine=None )
    #Create a normal font (for the rest)
    tmpFont=ImageFont.truetype( '/home/pi/.fonts/zx-spectrum.ttf', size=7, index=0, encoding="unic", layout_engine=None )
    oled.fill( 0 )
    oled.show()

if __name__ == "__main__":
    main()
