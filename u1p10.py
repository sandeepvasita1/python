lst=[10,20,30,40,50,60,70,80,90]
val=int(input("enter the number to find:"))

for f in lst:
    
    if f==val:
        print(f"{val} is found n list")
        break
else:
    print(f"{val} is not found in list")


