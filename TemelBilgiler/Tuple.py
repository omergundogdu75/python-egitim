
list = [1,2,3]
tuple = (1, 'iki', 3)

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(list))
print(len((tuple)))

list = ["ali","veli"]
tuple = ("damla","ayşe","damla")
names = ("damla1","ayşe2","damla1")
tuple = tuple + names

print(list)
print(tuple)


list[0] = "Ahmet"
# tuple[0] = "Ömer" tuplede atama yapılmaz

say = tuple.count("damla")

print(list)
print(say)
