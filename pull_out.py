import csv
import pandas as pd

# this is for pulling out all the credits for special edition for the first trilogy
# this means that all string in Note that continas 1997 or 2004 from the first 3 movies need to be pulled out

df = pd.read_csv('VI1983all.csv')

x = df["Note"].str.contains('2004')
print (x)

movie = (df[x == True])
movie.to_csv ('VI2004.csv', encoding='utf-8', index=False)
