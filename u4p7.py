import pandas as pd
data={"name":["sandeep","suhani","priya","khushi"],
      "city":["surat","baroda","ahmedabad","rajasthan"]}

df=pd.DataFrame(data)
print(df)

d=df['city']
print(d)
