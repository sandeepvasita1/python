import pandas as pd

data={'category':['a','b','c','d'],
      'value':[10,20,30,40]}

df=pd.DataFrame(data)
print(df)

df1=df.groupby('category')['value'].first()
print(df1)

df1=df.groupby('category')['value'].mean()
print(df1)

df1=df.groupby('category')['value'].min()
print(df1)

df1=df.groupby('category')['value'].max()
print(df1)
