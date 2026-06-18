import array as ar
arr=ar.array('i',[2,5,8,7,9,2,1,6,7,5])

print(arr)

se=int(input("enter value to be search:"))

if se in arr:
    p=arr.index(se)
    print(f"{se} value position is {p}")

else:
    print(f"{se} value position is not found")
