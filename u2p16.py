Create a dictionary that will accept cricket players name and 
scores in a match. Also we are retrieving runs by entering the 
player’s name. 
p={'kohli':105,'dhoni':150,'rohit':200,'sachin':250}
print(p)

search=input("enter player name for search")

runs=p.get(search)

if search in p:
    print(f"{search} run is {runs}")
else:
    print(f"{search} run is not found")
