Write a program to create a list using range functions and 
perform append, update and delete elements operations 
in it. 
  
lst=list(range(1,15))
print("print element",lst)

lst.append(25)
print("add new elements",lst)

lst[5]=45
print("add new element in",lst)

del lst[7]
print("delect element",lst)

lst.remove(10)
print("remove element",lst)
