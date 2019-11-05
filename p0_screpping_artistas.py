
import requests
from bs4 import BeautifulSoup
import re

"https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Cuba",
"https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_El_Salvador",
"https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Nicaragua"
"https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Honduras",


paises_rock_hispano_hablantes = [ "https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Argentina","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Guatemala","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Ecuador","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Costa_Rica","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Colombia","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Uruguay","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Per%C3%BA","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_del_Paraguay","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Panam%C3%A1","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_M%C3%A9xico","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Venezuela","https://es.wikipedia.org/wiki/Categor%C3%ADa:Grupos_de_rock_de_Bolivia"]

all_artist= []
all_artist_clean = []
for i in paises_rock_hispano_hablantes:
    print(i)
    all_about = requests.get(i)
    all_about_s = BeautifulSoup(all_about.text, "lxml")
    grupos = all_about_s.find_all("div", {"class": "mw-category-group"})
    for j in grupos :
        all_artist.append(    re.findall ("title=\"[0-9A-Za-z ÁÉÍÓÚáéíóú\(\ñÑ)\'¡!]*\"", str(  j )) )

all_artist_clean = []
for i in all_artist:
    if len(i) >=1:
        for j in i:
            all_artist_clean.append('https://genius.com/search?q=\"'+re.findall("[0-9A-Za-z ÁÉÍÓÚáéíóú\(\ñÑ)\'¡!]*" ,j)[3].strip()+"\"")
            
for i in all_artist_clean:
i=all_artist_clean[0]
all_about = requests.get(i)
all_about_s = BeautifulSoup(all_about.text, "lxml")
print(str(i )+"    "+ str(len(str(all_about_s)))+ "   " +str( all_about_s.find_all("a",{"set-class-before-navigate": "mini_card--active"} ) )) 



<a ng-href="https://genius.com/artists/2-minutos" class="mini_card" set-class-before-navigate="mini_card--active" href="https://genius.com/artists/2-minutos">
  <div class="mini_card-thumbnail">
    <div class="user_avatar user_avatar--large clipped_background_image--background_fill clipped_background_image" clipped-background-image=":: $ctrl.artist.image_url" style="background-image: url(&quot;https://t2.genius.com/unsafe/48x48/https%3A%2F%2Fimages.genius.com%2Fa059000b0c4c720fbda4ed3dc4e2d390.720x720x1.jpg&quot;);"></div>
  </div>
  <div class="mini_card-info mini_card-info--centered">
    <div class="mini_card-title">2 Minutos</div>
  </div>
</a>