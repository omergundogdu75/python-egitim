# hata yönetimi

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x / y)
# except ZeroDivisionError:
#     print("Sayı sıfıra bölünemez")
# except ValueError:
#     print("Lütfen sayısal bir değer giriniz")

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x / y)
    except Exception as e:
        print(e)
    else: # exception çalışmadığında bu kısıma giriş yapar
        break
    finally:
        print("Except sonlandı")

