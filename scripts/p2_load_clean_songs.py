import os, json
import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
path_to_json = '/home/ator97/Documents/git/npl_music/artist'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
jsons_data = pd.DataFrame(columns=['title', 'album', 'year','lyrics','artist'])
for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)
        title = json_text['songs'][0]['title']
        album = json_text['songs'][0]['album']
        year = json_text['songs'][0]['year']
        lyrics = json_text['songs'][0]['lyrics']
        artist = json_text['artist']
        jsons_data.loc[index] = [title, album, year, lyrics, artist]
#print(jsons_data)
clean_song= []
for i in range(0,7954):
    p0 = re.sub( '\n'                                                                           , ' ', jsons_data.at[i,'lyrics'].lower()) 
    p1 = re.sub( '\[[\*¿?!¡\[\]\+\-\"\'\(\)\/\+¿?!¡\.\"\:,;\/\\\'\&$“”’öüñèáéíóúa-z0-9 ]+\]'    , ' ', p0 )
    p2 = re.sub( '\([°\*—\[\]\+\-\"\'\(\)\/\+¿?!¡\.\"\:,;\/\\\'\&$“”’öüñèáéíóú…´a-z0-9 ]+\)'   , ' ', p1 )
    p3 = re.sub( '[\(\)\[\]\+¿?!¡\.\":,;\/\\\'-=]+'                                             , ' ', p2 )
    clean_song.append(re.sub('[ ]+', ' ', p3.strip()))

#print(len(clean_song))
jsons_data["cleanSong"]=clean_song
jsons_data   

for i in range (0,7954):
    print("------------------------------")
    print(jsons_data.at[i,'title'])
    tokens = [t for t in jsons_data.at[i,'cleanSong'].split()]
    clean_tokens = tokens[:]
    sr = stopwords.words('spanish')
    for token in tokens:
        if token in stopwords.words('spanish'):
            clean_tokens.remove(token)
    freq = nltk.FreqDist(tokens)
    for key,val in freq.items():
        print (str(key) + ':' + str(val))
    