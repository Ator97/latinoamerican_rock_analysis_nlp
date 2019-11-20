
import pandas as pd  
import numpy as np
import matplotlib as mpl 
import matplotlib.pyplot as plt
#Lectura de los datos previamente limpiados
master_path='/home/ator97/Documents/git/npl_music/'
data = pd.read_csv(master_path+"clean_songs.cvs")
data_years = data[data.year.notna()]
label= []
data_to_plot  = []
years_l = data_years.groupby('year').groups.keys()
for i in years_l:
        print()
        x = [i for i in data_years.loc[data_years['year'] == i][['compression_rate']].values]
        x = [float(np.array_str(i)[1:-1]) for i in x]
        if len(x) > 1:
                data_to_plot.append(np.array(x))
                label.append(str(int(i)))


fig = plt.figure(1, figsize=(50,30))
# Create an axes instance
ax = fig.add_subplot(111)
# Create the boxplot
bp = ax.boxplot(data_to_plot,labels= label)
# Save the figure
fig.savefig(master_path+'images/compression_plot.png', bbox_inches='tight')
