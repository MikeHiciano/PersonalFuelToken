import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image , ImageDraw , ImageFont

import subprocess

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

    - precio de los combustibles (Listo)
    - cambio de moneda (en proceso)
    - informacion rpi (en proceso)
    - cambio por boton (no iniciado)

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

datos = []

def datagas():
    my_url = 'https://micm.gob.do/precios-de-combustibles' #the victim
    uclient = uReq(my_url) #when u kidnap the victim
    page_html = uclient.read() #when u rape the victim
    uclient.close() #when u kill the victim
    soup =  Soup(page_html, "html.parser")

    titulo = soup.find_all('title')[0].get_text()
    tema = soup.find_all('h2')[0].get_text()

    for i in range(0,12):
        # print(soup.find_all('td')[i].get_text())
        datos.append(soup.find_all('td')[i].get_text())

if __name__ == '__main__':

    datagas()
    draw.text((x, top), "Precios Combustibles", font=font, fill=255)
    draw.text((x, top+16), "Gas. Prm.: " + str(datos[1]), font=font , fill=255)
    draw.text((x, top+25), "Gas. Reg.: " + str(datos[3]), font= font , fill=255)
    draw.text((x, top+32), "Die. Opt.: " + str(datos[5]) , font=font , fill=255)
    draw.text((x, top+40), "Die. Reg.: " + str(datos[7]) , font=font , fill=255)
    draw.text((x, top+48), "Kerosene:  " + str(datos[9]) , font=font , fill=255)
    draw.text((x, top+56), "GLP:       " + str(datos[11]) , font=font , fill=255)

    disp.image(image)
    disp.display()
    time.sleep(.1)