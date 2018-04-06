# python 3 

import pandas as pd
import numpy as np 
import os 



#riplets_file = 'https://static.turi.com/datasets/millionsong/10000.txt'
#songs_metadata_file = 'https://static.turi.com/datasets/millionsong/song_data.csv'
cwd = os.getcwd()
print (cwd)


# read data  1 
route_data_1 = cwd + '/data/usage_data.txt'
song_df_1 = pd.read_table(route_data_1,header=None)
song_df_1.columns = ['user_id', 'song_id', 'listen_count']
#print (song_df_1)

# read data  2 
route_data_2 = cwd + '/data/song_data.csv'
song_df_2 =  pd.read_csv(route_data_2)
# merge data 
song_df = pd.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")
# take a look 
print (song_df.head())






