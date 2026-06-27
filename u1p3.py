Write a program to create a byte type array, read, modify, and 
display the elements of the array 

arr=[15,20,12,45,3,11,85]

print(arr)

x=bytearray(arr)

for e in x:
    print(e)

print(x)

x[0]=33

print(list(x))
