sayi = int(input("Bir sayı giriniz:"))
asalMi = True
if sayi == 1:
    print("Sayı Asal değildir.")
else:
    for i in range(2, sayi):
        if (sayi % i == 0):
            asalMi = False
            break
            
    if asalMi:
        print(f"{sayi} Asaldır.")
    else:
        print(f"{sayi} Asal değildir.")