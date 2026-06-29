
Create a sample list of 7 elements and implement the List 
methods mentioned: append, insert, copy, extend, count, 
remove, pop, sort, reverse and clear.
lst=[7,8,5,2,6,3,4,1,2]
lst.append(40)
print(lst)

lst2=lst.copy()
print("list after copy",lst)

lst.extend(lst2)
print("extend liist",lst)

lst.remove(8)
print("list aftert remove",lst)

lst.pop()
print(lst)

print("count",lst.count(2))

lst.sort()
print("sorting",lst)


lst.reverse()
print("reverse lst",lst)
