#!/usr/local/bin/python

#
#Author         : Oscar Gutiérrez Castillo
#Creation Date  : 29-oct-2019
#Last Mod Date  : 29-oct-2019
#Description    : Genius web scraping with BeautifulSoup and requests
#

import requests
from bs4 import BeautifulSoup
import re

nombre="Charly-garcia"

print(nombre)
cantidad_discos=0
discos= []


#Obtenemos todos los discos del artista
all_about = requests.get('https://genius.com/artists/Charly-garcia')
all_about_s = BeautifulSoup(all_about.text, "lxml")


#soup.find_all("a", {"class": "full_width_button"})
#print("Disco: " + temp_nombre_disco)
    #Cada canción del disco en cuestion
    #######################################################################
#    for j in temp_album_s.find_all("a", {"class": "

#url con todos los albunes
all_albums='https://genius.com'+ all_about_s.find_all("a", {"class": "full_width_button",})[1].get('href')
req2 = requests.get(all_albums)
soup2 = BeautifulSoup(req2.text, "lxml")

albums= []

#print(soup.prettify())
###########################################################
for i in soup2.find_all("a", {"class": "album_link"}):   #
###########################################################
    canciones = []
    
    #i = soup2.find_all("a", {"class": "album_link"})[0]
    print("---------------------------------------")
    #Contamos los albunes del artista
    albums.append(i.get('href'))
    #Inspeccionamos cada disco
    temp_album='https://genius.com'+i.get('href')
    temp_album_req = requests.get(temp_album)
    temp_album_s = BeautifulSoup(temp_album_req.text, "lxml")
    #Proceso para obtener el nombre de cada disco
    str_algo=temp_album_s.find_all("h1", {"class": "header_with_cover_art-primary_info-title--white"})
    #temp_nombre_disco=b.group(0)[1:]

    #soup.find_all("a", {"class": imary_info-title header_with_cover_art-primary_info-title--white"})
    b = re.search(">\w*[ \w*]*",str(str_algo))
    temp_nombre_disco=b.group(0)[1:]
    print("Disco: " + temp_nombre_disco)
    #Cada canción del disco en cuestion
    #######################################################################
    for j in temp_album_s.find_all("a", {"class": "u-display_block"}):   #
    #######################################################################
    #j=temp_album_s.find_all("a", {"class": "u-display_block"})[0]
    #print(j.get('href'))
        temp_cancion_req = requests.get(j.get('href'))
        temp_cancion_s = BeautifulSoup(temp_cancion_req.text, "lxml")
        ##Nombre de la cancion
        str_nomre_cancion=temp_cancion_s.find_all("h1", {"class": "header_with_cover_art-primary_info-title "})
        b= re.search(">\w*[ \w*]*",str(str_nomre_cancion))
        temp_nombre_cancion=b.group(0)[1:]
        song = re.findall("[ \-,áéíóúñ¿?1!\(\)\w]+<b", str(temp_cancion_s))
        canciones.append(("[\"" + temp_nombre_cancion + "\" :\""+re.sub("[ ]+",' ',''.join(song).replace('<b', ' '), )+"\"]"))
    
    print(canciones)

    


#print(albums)

cantidad_discos= len(albums)
print(cantidad_discos)