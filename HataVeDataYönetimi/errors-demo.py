liste = ["1","2","5a","10b","abc","10","50"]

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

# while True:
#     sayi = input("Sayı: ")
#     if sayi == "q":
#         break
#     try:
#         result = float(sayi)
#         break
#     except ValueError:
#         print("Geçersiz Sayı!")
#         continue

# def checkPass(parola):
#     turkceKarakterler = "şçğüöıİÖĞÜ"
#     for i in parola:
#         if i in turkceKarakterler:
#             raise Exception("Parola Türkçe karakter içeremez.")
#         else:
#             pass
#     print("Geçerli Parola")
#
#
# parola = input("parola: ")
#
# try:
#     checkPass(parola)
# except TypeError as err:
#     print(err)


def faktoriyel(x):
    x = int(x)
    if x < 0:
        raise ValueError("Neğatif değer hatası")
    result = 1
    for i in range(1,x+1):
        result *= i

    return result

for x in [5,10,20,-3,"10a"]:
    try:
        y = faktoriyel(x)
        print(y)
    except Exception as e:
        print(e)



