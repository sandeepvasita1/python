cm=float(input("enter the length in cm:"))
if cm<0:
    print("invalid entry")

else:
    inch=cm/2.54
    print(f"{cm} is in{inch:.2f} inches")
