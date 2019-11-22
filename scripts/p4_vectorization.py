
import pandas as pd  
import re
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.spatial import distance
master_path='/home/ator97/Documents/git/npl_music/'
data = pd.read_csv(master_path+"clean_songs.cvs")
del data['Unnamed: 0']
del data['artist']
del data['album']
del data['year']
del data['compression_rate']
data2 = data.head(1500)

datas= []

for i in range (0,len(data2)):
    datas.append(data2.at[i,'cleanSongs'])

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(datas)
feature_names = vectorizer.get_feature_names()
dense = vectors.todense()
denselist = dense.tolist()
df = pd.DataFrame(denselist, columns=feature_names)

l2 = []

for i in range(0,46):
    l = []
    for j in range(0,46):
            if i > j :
                l.append(-1)
            else:
                l.append(distance.euclidean(df.iloc[i].tolist(),df.iloc[j].tolist()))
    if max(l) == 0:            
            l2.append(l)
    else:
        l = [i / max(l) for i in l]  
        l2.append(l)
    print("Vamos en :"+ str( i))


df_test=pd.DataFrame.from_records(l2)
print(df_test)

