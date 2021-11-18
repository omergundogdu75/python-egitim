# ogrenciler = {
#     "120" : {
#         "ad": "Ali",
#         "soyad":"Yılmaz",
#         "telefon":"532 000 00 01"
#     },
#     "125": {
#         "ad": "Can",
#         "soyad": "Korkmaz",
#         "telefon": "532 000 00 02"
#     },
#     "128": {
#         "ad": "Volkan",
#         "soyad": "Yükselen",
#         "telefon": "532 000 00 03"
#     },
# }

ogrenciler = {}


# ogrenciler [number] = {
#     "Ad" : name,
#     "Surname" : surname,
#     "Telefon" : phone
# }
number = input("Öğrenci no: ")
name = input("Öğrenci Adı: ")
surname = input("Öğrenci Soyadı: ")
phone = input("Öğrenci Telefon: ")

ogrenciler.update({
    number:{
        "ad":name,
        "surname":surname,
        "telefon":phone
    },
})


number = input("Öğrenci no: ")
name = input("Öğrenci Adı: ")
surname = input("Öğrenci Soyadı: ")
phone = input("Öğrenci Telefon: ")

ogrenciler.update({
    number:{
        "ad":name,
        "surname":surname,
        "telefon":phone
    },
})


number = input("Öğrenci no: ")
name = input("Öğrenci Adı: ")
surname = input("Öğrenci Soyadı: ")
phone = input("Öğrenci Telefon: ")

ogrenciler.update({
    number:{
        "ad":name,
        "surname":surname,
        "telefon":phone
    },
})

print(ogrenciler)

ogrNo = input("Öğrenci No: ")

ogrenci = ogrenciler[ogrNo]
print(f"Aradığınız  {ogrNo} nolu Öğrenci'nin Adı: {ogrenci['ad']} Soyadı: {ogrenci['surname']}"
      f"ve telefonu ise {ogrenci['telefon']} ")