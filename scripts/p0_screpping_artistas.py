
import requests
from bs4 import BeautifulSoup
import re


paises_rock_hispano_hablantes = [ "https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Argentina","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Guatemala","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Ecuador","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Costa_Rica","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Colombia","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Uruguay","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Per%C3%BA","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_del_Paraguay","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Panam%C3%A1","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_M%C3%A9xico","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Venezuela","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Bolivia"]

all_artist= []
all_artist_clean = []
#Obtenemos la lista de grupos musicales
for i in paises_rock_hispano_hablantes:
    all_about = requests.get(i)
    all_about_s = BeautifulSoup(all_about.text, "lxml")
    grupos = all_about_s.find_all("div", {"class": "mw-category-group"})
    for j in grupos :
        all_artist.append(    re.findall ("title=\"[0-9A-Za-z ÁÉÍÓÚáéíóú\(\ñÑ)\'¡!]*\"", str(  j )) )

#Limpiamos para poder tener los nombres de los artistas lo mas limpios posibles
all_artist_clean = []
for i in all_artist:
    if len(i) >=1:
        for j in i:
            all_artist_clean.append(re.findall("[0-9A-Za-z ÁÉÍÓÚáéíóú\(\ñÑ)\'¡!]*" ,j)[3])
            print(re.findall("[0-9A-Za-z ÁÉÍÓÚáéíóú\(\ñÑ)\'¡!]*" ,j)[3])

#Tenemos un total de 814 grupos latinoamericanos para analizar
#print(len(all_artist_clean))

#Buscamos en genius cuantos de los artistas  existen para pasar al paso p1 el cual permite descargar todas las letras de los artistas
#Los no existentes se anexan en otra lista

#artist_search_genius = []
#for i in all_artist_clean:
#  artist_search_genius.append('https://genius.com/search?q='+i.strip().replace(" ", "+"))
#  print('https://genius.com/search?q='+i.strip().replace(" ", "+"))
#

