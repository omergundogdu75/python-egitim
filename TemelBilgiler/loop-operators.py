# list = [1,2,3]
#
# for item in list:
#     print(item)

#range
# for item in range(10): # range(10)  0'dan 10'a kadar 10 dahil değil.
#     print(item)

# for item in range(2,10):  # range(10)  0'dan 10'a kadar 10 dahil değil.
#     print(item)

# for item in range(10,200,10):  # range(10)  0'dan 10'a kadar 10 dahil değil.
#     print(item)
# print(list(range(10,200,10)))

#enumarete ,
# greatings = "Hello There"
# index = 0
# for letter in greatings:
#     print(f"index: {index} letter:{letter} or letter: {greatings[index]}")
#     index += 1
#enumarate index değeri oluşturur.
# greatings = "Hello There"
# for index,letter in enumerate(greatings):
#     print(f"index: {index} letter:{letter} or letter: {greatings[index]}")
#     index += 1

# greatings = "Hello There"
# for item in enumerate(greatings):
#     print(item)



#zip

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

z = list(zip(list1,list2,list3))
print(z)

for item in z:
    print(item)

for a, b, c in z:
    print(a)