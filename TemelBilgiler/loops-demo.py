#random modülü
import random

rastgele = random.randint(1,100)
print(f"Rasgele Sayı: {rastgele}")
hak = 5
tahmin = int(input("Tahmin: "))

while tahmin != rastgele:
    hak -= 1
    if tahmin > rastgele:
        print(f"Tahmin ettiğiniz sayıyı azaltınız. Kalan hak:{hak}")
    elif tahmin<rastgele:
        print(f"Tahmin ettiğiniz sayıyı artırınız. Kalan hak:{hak}")

    tahmin = int(input("Tahmin: "))

print("Tebrikler. Sayıyı doğru tahmin ettiniz.")