import pandas as pd

df = pd.read_csv('ressources/combined.csv')

dups = df.pivot_table(columns=['name'], aggfunc= 'size')
dups.to_csv('ressources/dups.csv')
print(df['user_id'].nunique)