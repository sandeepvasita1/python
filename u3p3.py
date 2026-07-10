class student:
    def __init__(self):
        self.name=""
        self.rno=0

    def setname(self,n,rn):
        self.name=n
        self.rno=rn

    def getname(self):
        return self.name


    def getrno(self):
        return self.rno


s1=student()
s1.setname("sandeep",101)
print(s1.getname())
print(s1.getrno())
    
