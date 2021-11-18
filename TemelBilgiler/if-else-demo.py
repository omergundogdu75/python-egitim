# name = input("İsminiz: ")
# age = int(input("Yaşınız: "))
# egitim = input("Eğitim Bilgisi: ".lower())
#
# if (age >= 18) :
#     if ((egitim=="lise") or (egitim=="üniversite")):
#         print(f"Ehliyet alabilirsiniz")
#     else:
#         print(f"Ehliyet alamazsınız eğitim durumunuz yetersiz. {egitim} ")
# else:
#     print(f"Ehliyet alamazsınız. Yaşınız Küçük. {age}")

#--------------------------------------------------
# yazili1 = float(input("1.yazılı: "))
# yazili2 = float(input("2.yazılı: "))
# sozlu =  float(input("Sözlü: "))
# ortalama = (yazili2+ yazili1 + sozlu)/3
# if(ortalama>=0) and (ortalama<25):
#     print(f"Ortalama: {ortalama} - 1")
# elif (ortalama>=25) and (ortalama<50):
#     print(f"Ortalama: {ortalama} - 2")
# elif (ortalama >= 50) and (ortalama < 75):
#     print(f"Ortalama: {ortalama} - 3")
# elif (ortalama >= 75) and (ortalama <= 100):
#     print(f"Ortalama: {ortalama} - 4")
# else:
#     print(f"Geçersiz bilgi")
#
#--------------------------------------------------
# import datetime
# tarih = input("Aracınız hangi trafiğe çıktı? (2021/09/28)")
# tarih = tarih.split("/")
# trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
# simdi = datetime.datetime.now()
# print(simdi)
# fark = simdi-trafigeCikis
# days = fark.days
# print(fark.days)
#
# if days<=365:
#     print("1.servis aralığı")
# elif days>365 and days<=365*2:
#     print("2.servis aralığı")
# elif days*2 > 365 and days <= 365 *3:
#     print("3.servis aralığı")
# else:
#     print("Hatalı Süre")