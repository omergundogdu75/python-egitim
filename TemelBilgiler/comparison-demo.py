# a = int(input("a: "))
# b = int(input("b: "))
#
# result = (a>b)
# print(f"a: {a}, b: {b} den büyüktür: result:{result}")

# a = float(input("Vize1: "))
# b = float(input("Vize2: "))
# c = float(input("Final: "))
#
# ortalama = (((a + b)/2)*0.6 + c*0.4)
#
# print(f"Not Ortalamanız: {ortalama} ve dersten geçme durumunuz: {ortalama>50}")

# sayi = int(input("Sayı: "))
#
# tekcift = (sayi % 2 == 0)
#
# print(f"Girilen sayı çift olma durumu {tekcift}")

# sayi = int(input("Sayı: "))
#
# pozitifMi=(sayi>0)
#
# print(f"Girilen sayının pozitif olma durumu { pozitifMi}")

email = 'omergundogdu@gmail.com'
password = "abc123"

girilenEmail = input("E-mail: ")
girilenPassword = input("Parola: ")

isEmail = (email==girilenEmail.lower().strip())
isPass = (password==girilenPassword)

print(f"Girlen eposta durumu {isEmail} ve Girilen Şifre durumu {isPass}")