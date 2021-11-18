# # Hata nesnesi oluşturma
# x = 10
#
# if x>5:
#     raise Exception("X, 5 den büyük değer alamaz!")
#
# def checkPass(psw):
#     import re
#     if len(psw) < 8 :
#         raise Exception("Parola en az 8 karekler olmalıdır")
#     elif not re.search("[a-z]",psw):
#         raise Exception("Parola küçük harf içermelidir.")
#     elif not re.search("[A-Z]", psw):
#         raise Exception("Parola büyük harf içermelidir.")
#     elif not re.search("[0-9]", psw):
#         raise Exception("Parola sayı içermelidir.")
#     elif not re.search("[_@$]", psw):
#         raise Exception("Parola alfanümerik içermelidir.")
#     elif  re.search("[\s]", psw):
#         raise Exception("Parola boşluk içermemelidir.")
#     else:
#         print("Geçerli Parola")
#
#
# passwrd = "123456aA@78"
# try:
#     checkPass(passwrd)
# except Exception as e:
#     print(e)
# else:
#     print("Geçerli Parola else")
# finally:
#     print("Valitadion tamamlandı.")

class Person:
    def __init__(self,name,year):
        if len(name)>10:
            raise Exception("Name alanı fazla karekter içermektedir.")
        else:
            self.name = name

p = Person("ÖMER GÜNDOĞDU",1994)