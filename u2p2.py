import array as ar
arr=ar.array('i',[2,5,6,7,8,9,4])
print(arr)

arr.append(15)
print("Append",arr)

arr.insert(3,25)
print("insert",arr)

arr.remove(4)
print("remove",arr)

arr.pop()
print("pop",arr)

print("index:",arr.index(8))

print("tolist:",arr.tolist())

print("count:",arr.count(5))

print("length:",arr,len(arr))

