import os, json
import pandas as pd
import re
import subprocess
master_path='/home/ator97/Documents/git/npl_music/'
path_to_json = master_path+'artist'
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
    p0 = re.sub( '\n'                                                                               , ' ', jsons_data.at[i,'lyrics'].lower()) 
    p1 = re.sub( '\[[\*¿?!¡\[\]\+\-\"\'\(\)\/\+¿?!¡\.\"\:,;\/\\\'\&$“”’öüñèáéíóúa-z0-9 ]+\]'        , ' ',p0   )
    p2 = re.sub( '\([°\*—\[\]\+\-\"\'\(\)\/\+¿?!¡\.\"\:,;\/\\\'\&$“”’öüñèáéíóú…´a-z0-9 ]+\)'       , ' ',p1   )
    p3 = re.sub( '[\(\)\[\]\+¿?!¡\.\":,;\/\\\'-=»«]+'                                                , ' ',p2   )
    p4 = re.sub( ','                                                                                , ' ',p3   )
    clean_song.append(re.sub('[ ]+', ' ', p4.strip()))
    
#Agregamos cancion limpia
jsons_data["cleanSongs"]=clean_song
#Eliminamos todas las canciones con letras muy pequeñas o inexistentes
jsons_data = jsons_data.loc[ jsons_data['cleanSongs'].str.split().str.len() > 30] 
#Dejamos solo el año de release
jsons_data['year'] = jsons_data['year'].str.slice(0,4)
jsons_data = jsons_data[['artist','album','year','title','cleanSongs']]
#Reinicio de indice
jsons_data = jsons_data.reset_index()
del jsons_data['index']
#Getting compression level
songs = jsons_data[['cleanSongs']]
compression_rate=[]
#
for i in range (0,len(songs)):
    f=open(master_path+'compress/'+str(i)+'.txt',"w+")
    f.write(songs.at[i,'cleanSongs'])
    f.close()
    os.system("gzip "+master_path+'compress/'+str(i)+'.txt')
    compression_rate.append( subprocess.check_output("gzip -l "  +master_path+"compress/"+str(i)+".txt.gz"+  " | tail -1 | awk {'print $3'}", shell=True)[:-2].decode("utf-8") )
    os.system("rm "+ master_path+"compress/"+str(i)+".txt.gz")
jsons_data["compression_rate"]=compression_rate
export_csv = songs.to_csv(master_path+'clean_songs.cvs')
