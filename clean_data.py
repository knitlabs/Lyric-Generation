import pandas
import os

def lyrics_csv_by_genre():
    os.makedirs("lyrics",exist_ok=True)
    lyrical_data = pandas.read_csv("lyrics.csv")
    lyrical_data.drop(lyrical_data[lyrical_data['genre']=='Not Available'].index,inplace=True)
    lyrical_data.drop(['index','song','year','artist'],inplace=True,axis=1)

    genres = list(set(lyrical_data['genre']))
    lyrics = {}

    for i in genres:
        path = "lyrics/" + i + ".csv" 
        lyrics[i] = lyrical_data[lyrical_data['genre'] == i].drop('genre',axis=1)
        lyrics[i].dropna(inplace=True)
        lyrics[i].to_csv(path)


lyrics_csv_by_genre()