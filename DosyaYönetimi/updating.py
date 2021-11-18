#
# with open("newfile.txt", "r+", encoding="utf-8") as file:  # okuma ve yazma modu
#     file.seek(20)
#     file.write("Selam")
# with open("newfile.txt", "r+", encoding="utf-8") as file:  # okuma ve yazma modu
#      print(file.read())
# with open("newfile.txt", "a", encoding="utf-8") as file:  # sayfa sonuna metineklme
#     file.write("\nGND TECH")
# with open("newfile.txt", "r+", encoding="utf-8") as file:
#      print(file.read())

# with open("newfile.txt", "r+", encoding="utf-8") as file:  # sayfa başına metineklme
#     content = file.read()
#     content = "Mechatronic\n" + content
#     file.seek(0)
#     file.write(content)
#     print(content)

with open("newfile.txt", "r+", encoding="utf-8") as file:  # sayfa ortası güncelleme
    content = file.readlines()
    # help(list.insert)
    content.insert(1,"MIT")
    file.seek(0)
    file.writelines(content) # listeyi dosyaya yazar
    # for i in content:
    #     file.write(i)
    # print(content)

with open("newfile.txt", "r+", encoding="utf-8") as file:
     print(file.read())
