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

datos = {}

def datagas():
    url = 'https://micm.gob.do/direcciones/combustibles' #the victim
    uclient = uReq(url) #when u kidnap the victim
    page_html = uclient.read() #when u rape the victim
    uclient.close() #when u kill the victim
    soup =  Soup(page_html, "html.parser")

    data = []

    def datas():
        for i in range(1):
            data.append(soup.find_all('tbody')[i].get_text())
    
    datas()
    
    gas_prm = data[0][0:16]
    gas_prm_pr = data[0][16:26]
    gas_reg = data[0][26:42]
    gas_reg_pr = data[0][42:52]
    gsl_opt = data[0][52:65]
    gsl_opt_pr = data[0][65:75]
    gsl_reg = data[0][75:89] 
    gsl_reg_pr = data[0][89:99]
    krs = data[0][99:107]
    krs_pr = data[0][107:117] 
    glp = data[0][142:145]
    glp_pr = data[0][146:156]
    gnv = data[0][156:183]
    gnv_pr = data[0][183:193]

    strings = ['gasolina_premium','gasolina_regular','gasoil_optimo','gasoil_regular','kerosene','glp','gnv']
    price = [gas_prm_pr,gas_reg_pr,gsl_opt_pr,gsl_reg_pr,krs_pr,glp_pr,gnv_pr]
    for i in range(len(strings)):
        datos.setdefault(strings[i],price[i])

if __name__ == '__main__':

    datagas()
    draw.text((x, top), "Precios Combustibles", font=font, fill=255)
    draw.text((x, top+16), "Gas. Prm.: " + str(datos['gasolina_premium']), font=font , fill=255)
    draw.text((x, top+25), "Gas. Reg.: " + str(datos['gasolina_regular']), font= font , fill=255)
    draw.text((x, top+32), "Die. Opt.: " + str(datos['gasoil_optimo']) , font=font , fill=255)
    draw.text((x, top+40), "Die. Reg.: " + str(datos['gasoil_regular']) , font=font , fill=255)
    draw.text((x, top+48), "Kerosene:  " + str(datos['kerosene']) , font=font , fill=255)
    draw.text((x, top+56), "GLP:       " + str(datos['glp']) , font=font , fill=255)

    disp.image(image)
    disp.display()
    time.sleep(.1)