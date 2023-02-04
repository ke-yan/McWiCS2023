import pandas as pd
df1 = pd.read_csv('ressources/product_reviews.csv')
df1.head(1)
df1.drop(['age','skin_tone','brand_id','product_id','eye_color', "price"],axis=1,inplace=True)
print(df1.head(1))
df1.to_csv('ressources/reviews.csv')

df2 = pd.read_csv('ressources/product_types.csv')
df2.head(1)
df2.drop(['no_reviews','hearts','size1','size2','final_size','price_per_ounce', 'brand'],axis=1,inplace=True)
print(df2.head(1))
df2.to_csv('ressources/type.csv')

temp=pd.merge(df1, df2, on='name', how='inner')
temp.to_csv('ressources/combined.csv')
