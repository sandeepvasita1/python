while True:
    print("1: Area of circle")
    print("2: Area of triangle")
    print("3: Area of square")
    print("4: simple intrest")
    print("5: exit")

    m=int(input("enter your choice"))
    match(m):

                case 1:
                    r=int(input("enter the radius of circle:"))
                    area=3.14*(r**2)
                    print("Area of circle is:",area)

                case 2:
                    b=int(input("enter base of triangle"))
                    h=int(input("enter height of triangle"))
                    area=0.5*b*h
                    print("Area of triangle is:",area)

                case 3:
                    s=int(input("enter side of square"))
                    area=(s**2)
                    print("Area of square is:",area)

                case 4:
                    p=int(input("enter the principle amount:"))
                    r=int(input("enter the rate amount:"))
                    n=int(input("enter the no of year:"))
                    i=(p*r*n)/100
                    print("simple intrest is:",i)

                case 5:
                    print("exit")
                    break
                case _:
                    print("invalid choice:")
         
        
