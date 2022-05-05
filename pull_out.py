import csv
import pandas as pd

# this is for pulling out all the credits for special edition for the first trilogy

df = pd.read_csv('VI1983all.csv')

x = df["Note"].str.contains('2004')
print (x)

movie = (df[x == True])
movie.to_csv ('VI2004.csv', encoding='utf-8', index=False)
