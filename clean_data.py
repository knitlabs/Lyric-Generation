import pandas
from fastai.text import *

lyrical_data = pandas.read_csv("lyrics.csv")

lyrical_data.drop(lyrical_data[lyrical_data['genre']=='Not Available'].index,inplace=True)

genres = list(set(lyrical_data['artist']))
print(len(genres))
# print(Counter(genres))

# lyrical_data.drop(['index','song','year','artist'],inplace=True,axis=1)

# #print(lyrical_data.head())

# genres = set(lyrical_data['genre'])

# lyrics = {}

# for i in genres:
#     path = "lyrics/" + i + ".csv" 
#     lyrics[i] = lyrical_data[lyrical_data['genre'] == i].drop('genre',axis=1)
#     lyrics[i].dropna(inplace=True)
#     lyrics[i].to_csv(path)


