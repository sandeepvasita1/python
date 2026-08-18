class A:
    def display(self):
        print("This is Super Class method")


class B(A):
    def display(self):
        print("This is Sub Class method")


obj = B()
obj.display()
