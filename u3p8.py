class parent:
    def __init__(self,name):
        self.name=name

    def display(self):
        print("base class:",self.name)

class child(parent):
    def __init__(self,name,rno):
        super().__init__(name)
        self.rollno=rno

    def display(self):
        super().display()
        print("sub class:",self.rollno)

c1=child("sandeep",105)
c1.display()
