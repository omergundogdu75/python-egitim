# open(dosyaismi,dosyaerismemodu)
# w write yazma Dosyayı konumda oluşturur. / dosya içeriğini siler yenisini ekler.
# a append ekleme modu Dosyayı konumda oluşturur
# x create oluşturma. Dosya varsa hata verir.
# r read okuma. varsayılan. dosya konumda yoksa hata verir

# file = open("newfile.txt","w")
# file.close()

# file = open("C:/Users/OMERGUNDOGDU/Desktop/newfile.txt","w")

# file = open("newfile.txt","w",encoding="utf-8")
# file.write("Merhaba Txt dosyası")
# file.close()
# print(file)

#
# file = open("newfile.txt","a",encoding="utf-8")
# file.write(" 2021")
# file.close()


# file = open("newfile1.txt","x",encoding="utf-8")
# file.close()


file = open("newfile.txt","r",encoding="utf-8")
print(file)
