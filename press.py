import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image , ImageDraw , ImageFont

import bs4
from urllib.request  import urlopen as uReq
from bs4 import BeautifulSoup as Soup

'''
    RPi presentation program!

    Este programa consta de una presentacion de mi trabajo tanto como programador como de 
    maker, este programa consta de 3 partes , una hace el scrap para los precios de combustibles
    , el otro hace el scrap para el cambio de monedas (Dolares y euros), y la otra , contiene 
    la informacion de la raspberry pi , a continuacion una lista con lo que esta listo y lo
    que no:

    - presentacion (Listo)
    - precio de los combustibles (Listo)
    - cambio de moneda (en proceso (bug))
    - informacion rpi (en proceso)
    - cambio por boton (en proceso)

    maded by @h.iciano
'''

RST = None

DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1',(width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height),outline=0,fill=0)

padding = -2
top = padding
bottom = height-padding

x = 0

font = ImageFont.load_default()

if __name__ == '__main__':

    disp.clear()
    draw.text((x, top), "Hi Everyone", font=font, fill=255)
    draw.text((x, top+25), "-My name is Mike", font= font , fill=255)
    draw.text((x, top+32), "-I do this kind of", font=font , fill=255)
    draw.text((x, top+40), "stuffs ", font=font , fill=255)
    draw.text((x, top+56), "*Press the button*" , font=font , fill=255)
    
    disp.image(image)
    disp.display()
    time.sleep(.1) 


    
   
    