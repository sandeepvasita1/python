class Sum:
    def add(self, a, b, c=0):
        return a + b + c


s = Sum()

print("Sum of two numbers:", s.add(10, 20))
print("Sum of three numbers:", s.add(10, 20, 30))
