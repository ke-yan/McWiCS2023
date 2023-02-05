
import pandas as pd

df = pd.read_csv('ressources/combined.csv')

dups = df.pivot_table(columns=['name'], aggfunc= 'size')
dups.to_csv('ressources/dups.csv')
print(df['user_id'].nunique)

def hi():
    print('hello world')

def getTopProducts(profile,category,dataframe):
    user_type = profile[0]
    user_concern = profile[1]
    dataf = dataframe[(dataframe.skin_type == user_type) & (dataframe.skin_concerns == user_concern) & (dataframe.category==category)]
    dataf.drop(dataf.columns[[0]], axis=1, inplace=True)

    # Create user-item matrix
    matrix = dataf.pivot_table(index='user_id', columns='name', values='rating')
    matrix.head()
    # matrix.to_csv('ressources/test.csv')

    # Normalize user-item matrix
    matrix_norm = matrix.subtract(matrix.mean(axis=1), axis = 'rows')
    matrix_norm.head()
    matrix_norm.to_csv('ressources/test.csv')

    number_of_users = matrix.shape[0]
    # print(number_of_users)

    mean = matrix_norm.mean(axis=0)
    # print(mean)

    top = mean.nlargest(20)
    # print(top)
    top_ten_df = pd.DataFrame({'name':top.index, 'score':top.values})
    # print(top_ten_df.loc[:, 'name'].to_string(index=False))
    # top_ten_df.loc[:, 'name'].to_csv('ressources/test_top_10.csv',index=False)

    print(top_ten_df.loc[:, 'name'].to_numpy())
    return top_ten_df.loc[:, 'name'].to_numpy()

def getRecs(profile,has_treatment,has_mask,has_lip,has_eye):
    products =[]
    product_types_df = pd.read_csv('ressources/product_types.csv')

    categories = ["cleanser", "moisturizing-cream-oils-mists", "sunscreen-sun-protection"]
    if has_treatment:
        categories.append("facial-treatments")
    if has_mask:
        categories.append("facial-treatments-masks")
    if has_lip:
        categories.append("lip-treatments")
    if has_eye:
        categories.append("eye-treatment-dark-circle-treatment")
    
    # make df with name and price of each product
    for c in categories:
         top = getTopProducts(profile, c, df)
         for t in top:
            product_types_df.loc[df['name'] == t]
            # products.append

# def greedy (min, max, products) :
#     routine = pd.DataFrame(columns = ['type', 'name', 'price', 'url'])
#     routine = routine.append({'type' : '', 'name' : '', 'price' : '', 'url' : ''},
#         ignore_index = True)

#     cost = 0
#     for category in __ :
#         for info in _ :
#             if cost + info[1] < max :
#     return(routine)
    



# profile = ["combination", 'acne']
# getTopProducts(profile, 'facial-treatments', df)