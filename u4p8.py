import pandas as pd
data={"name":["sandeep","suhani","priya","khushi"],
      "age":[20,19,21,22],
      "score":[99,98,75,88]}

df=pd.DataFrame(data)
print(df)

df1=df.sort_values('score',ascending=False)
print(df1)
