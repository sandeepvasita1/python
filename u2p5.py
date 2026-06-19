def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True           
num=int(input("enter number for prime:"))

for i in range(2,num+1):
    if prime(i):
        print(i,end=" ")
