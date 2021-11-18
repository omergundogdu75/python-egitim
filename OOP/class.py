# class Person:
#     pass # yer tutucu
#
#     # attributes
#     # class atributes:
#     adress = "No Info"
#     # object atributes: constructor() yapıcı method içerisinde tanımlanır
#     def __init__(self,name,year):
#         self.name = name
#         self.year =year
#         print("İnit metodu çalıştı")
#     #instance methods
#     def intro(self):
#         print(f"Hello There {self.name}")
#     def calculate(self):
#         return 2021-self.year
#
# p1= Person("Ömer",1994)
# p2 = Person("GND",2021)
# #updating object
# p1.name="GÜNDOĞDU"
# p1.intro()
# #accessing object
# print(f"name: {p1.name} year: {p1.year} yas: {p1.calculate()} adress: {p1.adress}")
# print(f"name: {p2.name} year: {p2.year} yas: {p2.calculate()}  adress: {p2.adress}")
#
#
#
# # print(p1)
# # print(p2)
# #
# # print(type(p1))
# # print(type(p2))
# #

class Circle:
    #Class object atribute
    pi = 3.14

    def __init__(self,r=1):
        self.r = r

    def cevre_hesapla(self):
        return 2*self.pi*self.r

    def alan_hesapla(self):
        return self.pi*(self.r**2)

c1 = Circle()
c2 = Circle(5)

print(f"C1: alan = {c1.alan_hesapla()} cevre:{c1.cevre_hesapla()}")
print(f"C2: alan = {c2.alan_hesapla()} cevre:{c2.cevre_hesapla()}")