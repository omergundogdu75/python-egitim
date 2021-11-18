#fonksiyon tanımlamak için def kullanılır
def sayHello(name = "USER"):
    print(f"Hello {name}")

#fonksiyon tanımlamak için def kullanılır
def sayHello1(name = "USER"):
     return (f"Hello {name}")

sayHello("Ömer")
sayHello("GÜNDOĞDU")
sayHello("GND")
msg = sayHello1()
print(msg)

def total(num1,num2):
    return num1+num2

result = total(10,20)
print(result)

def yasHesapla(dogumYili):
    return 2021-dogumYili

age= yasHesapla(1994)
print(age)


def emekliligeKacYilKaldi(dogumYili,isim):
    '''
    Docstring: Doğum tarihine göre emeklilik hesaplama
    dogumYili: Doğum yılı giriniz
    isim: İsim giriniz

    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas
    if emeklilik>0:
        print(f"Emekliliğe {emeklilik} yaş kaldı.")
    else:
        print("Zaten emeklisiniz.")


emekliligeKacYilKaldi(1994,"Ömer")
print(help(emekliligeKacYilKaldi))
print(help(list.append))