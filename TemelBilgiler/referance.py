# value types -> string, number
x = 5
y = 25
x = y
y= 10

print(x,y)

# referance types-> list-class
a = ["Apple","Banana"]
b =  ["Apple","Banana"]
a = b

b[0] = "grape"
print(a,b)