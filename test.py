#import pandas as pd
#df = pd.read_csv('data.csv', header=0, index_col=2 )
#d = df.to_dict()
#print(d)

import csv
d = {}
with open('data.csv', mode='r') as f:
    data = csv.reader(f)
    for rows in data:
        d[rows[0]] = {'question': rows[1], 'answer': rows[2], 'points': rows[3]}
print(d)