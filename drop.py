import csv
import pandas as pd

#drop all the special edition credits

df = pd.read_csv('VI1983all.csv')


df.drop(df[df.Note.str.find('2004') != -1].index, inplace=True)

df.to_csv ('VI2004drop.csv', encoding='utf-8', index=False)
