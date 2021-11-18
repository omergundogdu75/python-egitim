# sayilar = [1,3,5,7,9,12,19,21]
# toplam = 0
# for sayi in sayilar:
#     if(sayi%2 == 1):
#         print(f"{sayi} sayısının karesi: {sayi**2}")

#     toplam += sayi
#     if(sayi%3==0):
#         print(f"{sayi}, 3'ün katıdır.")
#
#
# print(f"Sayıların toplamı {toplam}")

# ---------------------------------------------------------2
# sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]
# for sehir in sehirler:
#     karekterSayisi = len(sehir)
#     if(karekterSayisi<=5):
#         print(f"{sehir} isimli şehir, {karekterSayisi} karekterlidir.")

# ----------------------------------------------------------

urunler = [
    {"name":"samsung S6","price":"3000"},
    {"name": "samsung S7", "price": "4000"},
    {"name": "samsung S8", "price": "5000"},
    {"name": "samsung S9", "price": "6000"},
    {"name": "samsung S10", "price": "7000"}
]
# total = 0
# for urun in urunler:
#     total += int(urun['price'])
#
# print(f"Toplam Tutar: {total}")

for urun in urunler:
    if(int(urun['price']) <= 5000 ):
        print(f"{urun['name']} isimli ürünün fiyatı: {urun['price']}")