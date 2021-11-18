# try:
#     file = open("newfile.txt", "r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma hatası")
# finally:
#     print("Dosya kapandı")
#     file.close()
try:
    file = open("newfile.txt", "r",encoding="utf-8")
    # for i in file:
    #     print(i,end=".\n")
    # print("İçerik 1")
    # content1 = file.read()
    # print(content1) # dosya okuma işlemi tüm içerik
    #
    # print("İçerik 2")
    # content2 = file.read()
    # print(content2)
    # content = file.read(5)
    # content = file.read(3)
    #///////////////////////////////
    # content = file.readline() #tek satır okur
    # content = file.readline() #tek satır okur
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    #********** readlines: her satırı liste dizi elemanı olarak ele alr
    liste = file.readlines()
    print(liste)
    print(liste[0],"")
    print(liste[1],"")

except FileNotFoundError:
    print("Dosya okuma hatası")
finally:
    print("Dosya kapandı")
    file.close()


