Write a program to sort the array elements using bubble sort 
technique. 
import array as ar
arr=ar.array('i',[5,6,7,8,2,1,3,4])

n=len(arr)
print("length or array",n)

for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print("sorted array:",arr)            
