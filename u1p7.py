Write a program that evaluates an expression given by 
the user at run time using eval() function. Example: Enter and 
expression: 10+8-9*2- (10*2) Result: -20 

exp=input("Enter the number")
result = eval(exp)
print("Evalation of expression is:",result)
