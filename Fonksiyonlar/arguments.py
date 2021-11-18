# def changeName(n):
#     n = 'ada'
#
# name = "ÖMER"
# changeName(name)
# print(name)
# #-----------------------------------------
# def change(n):
#     n[0] = "İstanbul"
#
# sehirler = ["Ankara","İzmir","Antalya"]
# # change(sehirler)
# print(sehirler)
# # n = sehirler
# # n[0] = "Trabzon"
# # print(sehirler)
# # -----------------
#
# n1=sehirler[:] #slicing
# n1[0] = "Trabzon"
# print(sehirler)

# def add(*params):
#     return sum((params))
# print(add(10,20,30,50,70,20,50,1,60))

# def displayUser(**args):
#     print(type(args))
#     for key,value in args.items():
#         print(f"{key} {value}")
#
# displayUser(name = "ÖMER",age =2,city = "İstanbul")
# displayUser(name = "GüNDOĞDU",age =3,city = "Ankara",phone="123456")
# displayUser(name = "GND",age =4,city = "İzmir",phone="123412123",email="gnd@gmail.com")

def myFunc(a,b,c,*args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,key1="value1",key2="value2")