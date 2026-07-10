class student:
    count=0
    
    def __init__(self):
        student.count=self.count+1

    @staticmethod
    def display():
        print(student.count)

s1=student()
s2=student()
s3=student()
s4=student()

student.display()
