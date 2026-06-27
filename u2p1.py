Create a program to retrieve, display and update only a range 
of elements from an array using indexing and slicing in

import array as ar
arr=ar.array('i',[10,20,30,40,50,60,70,80])

print(arr)

for i in arr:
    print(i)

arr[3]=25
print(arr)

s=arr[3:6]
print(s)

for i in range(3,6):
    val=int(input("enter new value"))
    i=val
    arr[i]=val
    print(arr)
