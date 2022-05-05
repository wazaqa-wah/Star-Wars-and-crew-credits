import pandas as pd
import csv

#compare the datasets and find new credits

df_VI = pd.read_csv('VI1983all.csv')
df_I = pd.read_csv('I1999all.csv')

diff = ~df_I['Credit'].isin(df_VI['Credit'])
#later film first .earlier film later

#print(diff)

VI_I_diff = (df_I[diff == True])
#later film difference
VI_I_diff.to_csv('diff_VI_I.csv', encoding='utf-8', index=False)
