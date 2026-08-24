import pandas as pd

df=pd.DataFrame({'A':[1,None,3],'B':[None,4,5]})

print(df)
df1=df.fillna(0)
print(df1)
