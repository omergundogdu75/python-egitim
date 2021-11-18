# key value

# sehirler = ["İSTANBUL","KOCAELİ"]
# plakalar = [34,41]
#
# print(plakalar[sehirler.index("İSTANBUL")])
# print(plakalar[sehirler.index("KOCAELİ")])
#------------------------------------------

# plakalar = {"Kocaeli":41,"İstanbul":34}
#
# plakalar["Ankara"] = 6
# plakalar["İstanbul"] = "new value"
#
# print(plakalar["İstanbul"])
# print

users = {
    "Ömer Gündoğdu":{
        "age":27,
        "roles":["admin","user"],
        "email":"omergundogdu@gmail.com",
        "adress": "İstanbul",
        "phone" : "+90 538 283 68 73"
    },
    "Gnd Teknoloji":{
        "age": 2,
        "roles":  "user",
        "email": "gndteknoloji@gmail.com",
        "adress": "Türkiye",
        "phone": "+90 538 283 68 73"
    }
}

print(users["Ömer Gündoğdu"]["age"])
print(users["Ömer Gündoğdu"]["email"])
print(users["Ömer Gündoğdu"]["roles"][0])