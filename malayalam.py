
from fastai.text import *

x = ['Country.csv', 'Jazz.csv', 'R&B.csv', 'Hip-Hop.csv', 'Rock.csv', 'Folk.csv', 'Pop.csv', 'Metal.csv', 'Indie.csv', 'Other.csv', 'Electronic.csv']

country = TextLMDataBunch.from_csv(path = 'lyrics/',csv_name = x[0])
jazz = TextLMDataBunch.from_csv(path = 'lyrics/',csv_name = x[1])
rnb  =  TextLMDataBunch.from_csv(path = 'lyrics/',csv_name = x[2])
hiphop = TextLMDataBunch.from_csv(path = 'lyrics/',csv_name = x[3])
rock = TextLMDataBunch.from_csv(path = 'lyrics/',csv_name = x[4])
folk = TextLMDataBunch.from_csv(path = 'lyrics/',csv_name = x[5])
pop = TextLMDataBunch.from_csv(path = 'lyrics/',csv_name = x[6])
metal = TextLMDataBunch.from_csv(path = 'lyrics/',csv_name = x[7])
indie = TextLMDataBunch.from_csv(path = 'lyrics/',csv_name = x[8])
other = TextLMDataBunch.from_csv(path = 'lyrics/',csv_name = x[9])
electronic = TextLMDataBunch.from_csv(path = 'lyrics/',csv_name = x[10])

lyric_learner = language_model_learner(metal,AWD_LSTM) #Replace metal with required genre
lyric_learner.fit_one_cycle(3)


TEXT = ""     #Specify Inital words if any
N_WORDS = 215 #Specify number of words
print(lyric_learner.predict(TEXT,n_words=N_WORDS,temperature = 0.75).replace(',','\n'))