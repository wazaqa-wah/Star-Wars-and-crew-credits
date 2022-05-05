import csv
import pandas as pd

#drop all the special edition credits
# this means that any string in Note that contians 1997 or 2004 for the first 3 movies need to be dropped.

df = pd.read_csv('VI1983all.csv')


df.drop(df[df.Note.str.find('2004') != -1].index, inplace=True)

df.to_csv ('VI2004drop.csv', encoding='utf-8', index=False)
