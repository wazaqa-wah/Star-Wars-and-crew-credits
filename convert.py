import csv
import pandas as pd
import json

with open('IX_data.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)


df.to_csv('IX_data.csv', encoding='utf-8', index=False)
