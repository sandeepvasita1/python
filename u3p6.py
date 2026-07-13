class blank:
    def __init__(self,n,b):
        self.name=n
        self.bal=b

    def display(self):
        print("account name is:",self.name)
        print("balance is:",self.bal)


    def deposit(self,a):
        self.bal+=a
        print("deposite amount is:",a)
        print("deposite balance is:",self.bal)

    def withrawal(self,a):
        if self.bal>a:
            self.bal-=a
            print("deposit amount is:",a)
            print("current balance is:",self.bal)

        else:
            print("insufficient balance")
            
            
b1=blank("sandeep",7000)
b1.display()
b1.deposit(3000)
b1.withrawal(5000)
b1.withrawal(5000)

