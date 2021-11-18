# sayi = int(input("Sayı: "))
# result = 0< sayi <100
# result =  (sayi>0) and (sayi % 2==0)

# email = "asd@gmail.com"
# password = "123asd"
#
# girilenEmail = input("E-posta Adresiniz: ")
# girilenPassword = input("Parolanız: ")
# result = (girilenEmail == email) and (girilenPassword == passworda)
# print(result)
# a = int(input("SayıA: "))
# b = int(input("SayıB: "))
# c = int(input("SayıC: "))
# result = (a>b) and (a>c)
# print(f"a en büyük sayıdır: {result}")
# result = (c>b) and (c>b)
# print(f"c en büyük sayıdır: {result}")
# result = (a<b) and (b>c)
# print(f"b en büyük sayıdır: {result}")
# V1 = int(input("vize1: "))
# V2= int(input("vize2: "))
# F = int(input("final: "))
# ortalama = ((V1 + V2)*0.3 + F*0.4)
# result = ortalama >= 50  and F>50

name = input("Adınız: ")
kg = float(input("Kilonuz "))
hg = float(input("Boyunuz: "))
index = (kg) / hg**2

zayif = (index>=0) and (index<=18.4)
normal = (18.4 < index) and (index<=24.9)
kilolu = (index>24.9) and (index<=29.9)
obez = (index>29.9) and (index<= 34.9)

print(f"{name} Kilo indeksi: {index} ve kilo değerlendirmesi: zayıf: {zayif} ")
print(f"{name} Kilo indeksi: {index} ve kilo değerlendirmesi: normal: {normal} ")
print(f"{name} Kilo indeksi: {index} ve kilo değerlendirmesi:  Kilolu: {kilolu} ")
print(f"{name} Kilo indeksi: {index} ve kilo değerlendirmesi: obez {obez} ")


