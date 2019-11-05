#!/usr/local/bin/python

#
#Author         : Oscar Gutiérrez Castillo
#Creation Date  : 29-oct-2019
#Last Mod Date  : 4-nov-2019
#Description    : Genius web scraping with BeautifulSoup and requests
#

import requests
from bs4 import BeautifulSoup
import re

#Formato del json
nombre="\"Charly Garcia\""
print("{")
print("\t\"autor\":"+ nombre+",")
print ("\t\"discos\":")
print("\t{")

#Obtenemos todos los discos del artista
all_about = requests.get('https://genius.com/artists/Charly-garcia')
all_about_s = BeautifulSoup(all_about.text, "lxml")


#url con todos los albunes
all_albums='https://genius.com'+ all_about_s.find_all("a", {"class": "full_width_button",})[1].get('href')
req2 = requests.get(all_albums)
soup2 = BeautifulSoup(req2.text, "lxml")

albums= []
disco_s = soup2.find_all("a", {"class": "album_link"})
largo_disco = len(disco_s)

#Iteramos sobre cada disco para obtener las canciones
for i in disco_s: 
    largo_disco = largo_disco - 1

    canciones = []

    #Guardamos todas las ligas web de los albunes del artista, solo por 
    albums.append(i.get('href'))
    cantidad_discos= len(albums)

    #Inspeccionamos cada disco
    temp_album='https://genius.com'+i.get('href')
    temp_album_req = requests.get(temp_album)
    temp_album_s = BeautifulSoup(temp_album_req.text, "lxml")

    #Proceso para obtener el nombre de cada disco
    str_algo=temp_album_s.find_all("h1", {"class": "header_with_cover_art-primary_info-title--white"})
    b = re.search(">\w*[ \w*]*",str(str_algo))
    temp_nombre_disco=b.group(0)[1:]
    #Formato json del nombre del disco
    print("\t\t\"disco\":\"" + temp_nombre_disco+"\",")

    #Proceso para obtener la letra de cada cancion
    canciones_s = temp_album_s.find_all("a", {"class": "u-display_block"})
    largo_canciones = len(canciones_s)
    for j in canciones_s:
        largo_canciones = largo_canciones - 1
        temp_cancion_req = requests.get(j.get('href'))
        temp_cancion_s = BeautifulSoup(temp_cancion_req.text, "lxml")
    
        ##Nombre de la cancion
        str_nomre_cancion=temp_cancion_s.find_all("h1", {"class": "header_with_cover_art-primary_info-title "})
        b= re.search(">\w*[ \w*]*",str(str_nomre_cancion))
        temp_nombre_cancion=b.group(0)[1:]
        song = re.findall("[ \-,áéíóúñ¿?1!\(\)\w]+<b", str(temp_cancion_s))
        if largo_canciones >=1:
            canciones.append(("\"" + temp_nombre_cancion + "\" :\""+re.sub("[ ]+",' ',''.join(song).replace('<b', ' '), ).strip()+"\","))
        else:
            canciones.append(("\"" + temp_nombre_cancion + "\" :\""+re.sub("[ ]+",' ',''.join(song).replace('<b', ' '), ).strip()+"\""))

    #Formatos finales del json
    print("\t\t\"canciones\":{")
    for x in canciones:
        print("\t\t\t"+x)
    if largo_disco >=1:
        print("\t\t},")
    else:
        print("\t\t}")

#Cierre del json
print("\t},")
print("\t\"cantidad_discos\":"+str(cantidad_discos))
print("}")
