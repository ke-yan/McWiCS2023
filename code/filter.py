import pandas as pd

df = pd.read_csv('ressources/combined.csv')

dups = df.pivot_table(columns=['name'], aggfunc= 'size')
dups.to_csv('ressources/dups.csv')
print(df['user_id'].nunique)

def getRecs(array,product,dataframe):
    user_type = array[0]
    user_concern = array[1]
    dataf = dataframe[(dataframe.skin_type == user_type) & (dataframe.skin_concerns == user_concern) & (dataframe.category==product)]
    dataf.drop(dataf.columns[[0]], axis=1, inplace=True)

    dataf.to_csv('ressources/test.csv')

array = ["combination", 'acne']
getRecs(array, 'facial-treatments', df)