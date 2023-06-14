import numpy as np
import pandas as pd


data = pd.read_csv("datasets/imdb.csv")
df = pd.DataFrame(data)


result = df.head()

result = df.head(10)

result = df.tail()

result = df.tail(10)

result = df["Title"]

result = df["Title"].head()

result = df[["Title","imdbRating"]].head()

result = df[["Title","imdbRating"]].tail(7)

result = df[5:15][["Title","imdbRating"]].head()

result = df.query("imdbRating > 7.2")[["Title","imdbRating"]].head(50)

result = df.query("Year >= 2014 & Year <= 2015")["Title"]

result = df.query("tomatoReviews > 100.000 | imdbRating > 8 & imdbRating < 9")[["Title","imdbRating","tomatoReviews"]].head(20)

print(result)