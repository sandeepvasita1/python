a=[10,20,30]
b=a

print("Memory location of a:",id(a))
print("Memory location of b:",id(b))

if a is b:
    print("a and b are the same object.")
else:
    print("a and b are different objects.")

if a is not b:
    print("a and b are not the same object.")
else:
    print("a and b are the same object.")
