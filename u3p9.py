class parent:
    def __init__(self,name):
        self.name=name

    def display(self):
        print("base class:",self.name)

class student(parent):
    def __init__(self,name,rno):
        super().__init__(name)
        self.rollno=rno

    def display(self):
        super().display()
        print("sub class:",self.rollno)

class teacher(parent):
    def __init__(self,name,sub):
        super().__init__(name)
        self.subject=sub

    def display(self):
        super ().display()
        print("sub class:",self.subject)

c1=student("sandeep",105)
c1.display()
c1=teacher("suhani","python")
c1.display()
