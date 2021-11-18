x,y,z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

k = input("İlk sayıyı giriniz: ")
l = input("İkinci sayıyı giriniz: ")

total = int(k) * int(l) - (x + y+ z)
print(total)
print(y//x)
print((x + y + z )%3)
print(y**x)

x,*y,z = numbers

print(z**3)

yt = 0

for i in y:
    yt += i

print(yt)