class Number:
    def __init__(self, value):
        self.value = value

    # Overload + operator
    def __add__(self, other):
        return Number(self.value + other.value)

    def display(self):
        print("Sum =", self.value)

# Create objects
n1 = Number(10)
n2 = Number(20)

# Add objects
n3 = n1 + n2

# Display result
n3.display()
