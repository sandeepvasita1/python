class mother:
    def height(self):
        print("height is 5.6 ft")

class father:
    def color(self):
        print("color is brown")

class child(father,mother):
    def weight(self):
        print("weight is 65kg")

c1=child()
c1.height()
c1.color()
c1.weight()
        
    
