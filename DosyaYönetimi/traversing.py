#Farklı dosya okuma işlemleri
# file = open("newfile.txt","r",encoding="utf-8")
# content = file.read()
# print(content)
#
# file.close()

with open("newfile.txt","r",encoding="utf-8") as file: # with komutu: bu komut close yapmamıza gerek duymaz dosyayı kendisi kapatır.
    content = file.read()
    print(content)
    file.seek(0) # cursoru 0.konuma gönder 1880674
    print(file.tell()) # cursor konumu
    content2 = file.read()
    print(content2)
    print(file.tell())