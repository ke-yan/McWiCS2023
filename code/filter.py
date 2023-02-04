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

    # Create user-item matrix
    matrix = dataf.pivot_table(index='user_id', columns='name', values='rating')
    matrix.head()
    matrix.to_csv('ressources/test.csv')

    # Normalize user-item matrix
    matrix_norm = matrix.subtract(matrix.mean(axis=1), axis = 'rows')
    matrix_norm.head()
    matrix_norm.to_csv('ressources/test.csv')

    number_of_users = matrix.shape[0]
    # print(number_of_users)

    mean = matrix_norm.mean(axis=0)
    # print(mean)

    top_ten = mean.nlargest(10)
    print(top_ten)



array = ["combination", 'acne']
getRecs(array, 'facial-treatments', df)