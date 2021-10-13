import sys, os, netifaces, psutil, board, adafruit_ssd1306, time
from PIL import Image, ImageDraw, ImageFont

def getIP():
    return netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']


def getMEMFREE():
    return float( psutil.virtual_memory()[2] )


def getAVGLOAD():
    return os.getloadavg()


def getCPULOAD( tmpTime ):
    return psutil.cpu_percent( tmpTime )


def getCPUFREQ():
    return psutil.cpu_freq()[0]


def getCPUTEMP():
    return float( psutil.sensors_temperatures()['cpu_thermal'][0][1] )


def getDISKFREE():
    return psutil.disk_usage('/')[3]


def screensaver():
    return False


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

    while 1:
        oled.fill( 0 )
        #Create the image to be shown
        tmpImage=Image.new( "1", (oled.width, oled.height) )
        #Create a canvas
        tmpCanvas=ImageDraw.Draw( tmpImage )
        if ( not os.path.exists('/home/pi/autoexec/startup.pid')):
            #Construct the string
            tmpLAN="%s" % getIP()
            #Measure the string
            ( font_width, font_height ) = tmpFont.getsize( tmpLAN )
            #Put it onto the canvas
            tmpCanvas.text( (0,0), tmpLAN, font=tmpBoldFont, fill=255  )
            #Repeat as before with different values
            tmpCPU="CPU: %4.1fC %3.0fMz" % ( getCPUTEMP(), getCPUFREQ() )
            ( font_width, font_height ) = tmpFont.getsize( tmpCPU )
            tmpCanvas.text( (0,7), tmpCPU, font=tmpFont, fill=255  )
            #Another one...
            tmpRAM="RAM: %04.1f%% free" % ( getMEMFREE() )
            ( font_width, font_height ) = tmpFont.getsize( tmpRAM )
            tmpCanvas.text( (0,16), tmpRAM, font=tmpFont, fill=255  )
            #Yet another one...
            tmpHDD="HDD: %04.1f%% used" % ( getDISKFREE() )
            ( font_width, font_height ) = tmpFont.getsize( tmpHDD )
            tmpCanvas.text( (0,25), tmpHDD, font=tmpFont, fill=255  )
            #Load the image
            oled.image( tmpImage )
        else:
            tmpMessage="Booting..."
            ( font_width, font_height ) = tmpFont.getsize( tmpMessage )
            #Put it onto the canvas
            tmpCanvas.text( (0,0), tmpMessage, font=tmpBoldFont, fill=255  )
            #Load the image
            oled.image( tmpImage )
            os.remove('/home/pi/autoexec/startup.pid')
        #Switch planes.
        oled.show()
        time.sleep(20)

if __name__ == "__main__":
    main()
