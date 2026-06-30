tpl=((105,'sandeep',25000),
     (102,'suhani',20000),
     (101,'priya',30000),
     (104,'khushi',15000))
print(tpl)

for i in tpl:
    print(i)

print("sorted tuple:",sorted(tpl,reverse=True))
print("sorted tuple by name:",sorted(tpl,key=lambda x:x[1]))
print("sorted tuple by salary:",sorted(tpl,key=lambda x:x[2])) 
     
