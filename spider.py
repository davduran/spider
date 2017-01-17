#!/usr/bin/python
import os
import re
import time
import string
import random
import MySQLdb
import mechanize
from BeautifulSoup import BeautifulSoup  as bs
 
os.system("clear")
 
print """
  ******************************************************************************
  *                           SpiderBot v1.0 [2011]                            *
  ******************************************************************************
"""
 
print """
------------------------------------------------------------
 Analizando:
   - Fotocasa
   - Pisos.com
   - Idealista
   - Habitaclia
------------------------------------------------------------
"""
 
time.sleep(1.5)
 
os.system("clear")
 
print "Iniciando Browser..."
 
br = mechanize.Browser()
 
br.set_handle_robots(False)
 
useragent = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/2010020que Ubuntu/9.04 (Alegre) Namoroka/3.6.2pre ',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
        'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
            'Mozilla/5.0 (Windows; U; Windows NT 6.en-US-Urv rv:1.9.0.6)',
            'Microsoft Internet Explorer/4.0b1 (Windows 95)',
            'Opera/8.00 (Windows queT 5.1; U; en)',
        'Amaya/9.51 libwww/5.4.0',
        'Mozilla/4.0 (compatible; MSIE 5.0; AOL Windowsndows 95; c_athome)',
        'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (como Gecko) (Kubuntu)',
        'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]'
        ]
 
br.addheaders = [('User-agent', random.choice(useragent))]
 
# Venta de Viviendas en Fotocasa.es
print "Venta de Viviendas en Fotocasa.es\n"
 
try:
    respuesta = br.open("http://viviendas.fotocasa.es/")
except HTTPError, e:
    sys.exit("%d: %s" % (e.code, e.msg))
 
html = respuesta.read()
soup = bs(html)
 
texto = soup.findAll('li')
 
for i in range(7, 56):
    poblacion = string.replace(texto[-i].a.string,'Viviendas  en  venta  en  ','')
    link = texto[-i].a.get('href')
    anuncios = texto[-i].text
    anuncios = string.replace(anuncios,'(','')
    anuncios = string.replace(anuncios,')','')
    anuncios = string.replace(anuncios,'Viviendas  en  venta  en  '+poblacion,'')
 
    print poblacion
    print anuncios
    print link
    print "---------------------------"
 
# Alquiler de Viviendas en Fotocasa.es
print "\n\nAlquiler de Viviendas en Fotocasa.es\n"
 
try:
    respuesta = br.open("http://alquiler.fotocasa.es/")
except HTTPError, e:
    sys.exit("%d: %s" % (e.code, e.msg))
 
html = respuesta.read()
soup = bs(html)
 
texto = soup.findAll('li')
 
for i in range(7, 56):
    poblacion = string.replace(texto[-i].a.string,'Alquiler de viviendas  en  ','')
    link = texto[-i].a.get('href')
    anuncios = texto[-i].text
    anuncios = string.replace(anuncios,'(','')
    anuncios = string.replace(anuncios,')','')
    anuncios = string.replace(anuncios,'Alquiler de viviendas  en  '+poblacion,'')
 
    print poblacion
    print anuncios
    print link
    print "---------------------------"
 
 
# Compartir Viviendas en Fotocasa.es
print "\n\nCompartir Viviendas en Fotocasa.es\n"
 
try:
    respuesta = br.open("http://compartir.fotocasa.es/")
except HTTPError, e:
    sys.exit("%d: %s" % (e.code, e.msg))
 
html = respuesta.read()
soup = bs(html)
 
texto = soup.findAll('li')
 
for i in range(7, 56):
    poblacion = string.replace(texto[-i].a.string,'Viviendas a compartir  en  ','')
    link = texto[-i].a.get('href')
    anuncios = texto[-i].text
    anuncios = string.replace(anuncios,'(','')
    anuncios = string.replace(anuncios,')','')
    anuncios = string.replace(anuncios,'Viviendas a compartir  en  '+poblacion,'')
 
    print poblacion
    print anuncios
    print link
    print "---------------------------"
