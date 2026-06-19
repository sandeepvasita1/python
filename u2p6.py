def unique_val(lst):
    r=[]
    for i in lst:
        if i not in r:
            r.append(i)
    print(r)

            
lst1=[4,5,4,5,2,1,3,1,6,6]
unique_val(lst1)
