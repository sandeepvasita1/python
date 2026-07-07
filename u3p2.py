class student:
    clg_name=":pica"
    def __init__ (self,rno,n,m):
        self.rollno=rno
        self.name=n
        self.mark=m

    def display(self):
        print(f"student rollno is:{self.rollno}")
        print(f"student name is:{self.name}")
        print(f"student mark is:{self.mark}")
        print(f"collage name{student.clg_name}")
        print("")


s1=student(101,"sandeep",85)
s1.display()

s2=student(102,"suhani",78)
s2.display()
