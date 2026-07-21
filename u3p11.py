class Student:
    def display(self):
        print("Display method exists.")

class Teacher:
    def show(self):
        print("Show method exists.")


s = Student()
t = Teacher()


if hasattr(s, "display"):
    print("display() method exists in Student object.")
else:
    print("display() method does not exist in Student object.")

if hasattr(t, "display"):
    print("display() method exists in Teacher object.")
else:
    print("display() method does not exist in Teacher object.")
