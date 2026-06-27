Write  programs to demonstrate the use of Positional 
Argument, keyword argument , default arguments , variable 
length arguments

def pos(x,y):
    print(x+y)

a=2
b=3
pos(a,b)

def keyword(i,p):
    print("item",i)
    print("price",p)

keyword(i="sugar", p=35.4)
keyword(i="jaggery",p=78)


def default(i,j,p=70.5):
    print("item",i)
    print("bath item",j)
    print("price",p)

default(i="tea", j="soap")
default(i="grain",j="sampoo")

def abc(f,*f1):
    sum=0
    for i in f1:
        sum+=i
    print("sum of variable length:",sum)
    print("sum of formal+variable length:",f+sum)

abc(10)
abc(10,20)
abc(10,20,30)
