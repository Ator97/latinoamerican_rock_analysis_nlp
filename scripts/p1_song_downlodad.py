import sys
import lyricsgenius

archivo= sys.argv[1]

genius = lyricsgenius.Genius("zn_6Mzc6Z1wRMOATX02WxpYqlLLWrg5XHTGRkXPFS1Bgw6fA7InCiq8GMcyqsRmO")

f= open(archivo,"r")
log_file = archivo + "log"
log = open(log_file,"a")
log.write("No se encontro el grupo:")

for i in f:
    #print(i)
    try :
        artist = genius.search_artist(i, sort="title",allow_name_change =False)
        artist.save_lyrics()
    except:
        log.write(i)

log.close
f.close