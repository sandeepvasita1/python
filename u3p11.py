class a:
    def show(self):
        print("method of a")


class b:
    def show(self):
        print("method of b")        


class c:
    def show(self):
        print("method of c")


class d(b,c):
    pass
d1=d()
d1.show()

for i in d.__mro__:
    print(i)
