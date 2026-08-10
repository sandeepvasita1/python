class Student:
    def display(self):
        print("Display method exists.")

class Teacher:
    def show(self):
        print("Show method exists.")


s = Student()
t = Teacher()
print(type(s))
print(type(t))


if hasattr(s, "display"):
    print("display() method exists in Student object.")
else:
    print("display() method does not exist in Student object.")

if hasattr(t, "show"):
    print("show() method exists in Teacher object.")
else:
    print("show() method does not exist in Teacher object.")
