class student:
    clg_name="L.J college"

    def __init__(self,n,rn):
        self.name=n
        self.rno=rn

    @classmethod
    def data(cls,clg):
        cls.clg_name=clg

    def display(self):
        print("student name:",self.name)
        print("student rollno:",self.rno)
        print("college name:",self.clg_name)

s1=student("sandeep",101)
s1.display()
student.data("president")
s1.display()
