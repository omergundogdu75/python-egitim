mylist = [1,2,3]
# myString = "My String"
#
# print(len(mylist))
# print(len(myString))
#
# print(type(mylist))
# print(type(myString)print(type(myString)
class Movie:
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print(f"Movie oluşturuldu")

    def __str__(self):
        return f" {self.title} by {self.director}"
    def __len__(self):
        return  self.duration  # len
    def __del__(self):
        print("Film Silindi")

m = Movie("Film Adı","Yönetmen",120)

# print(mylist)
# print(str(m))

print(len(mylist))
print(len(m))

del m
# m  objesi silindi

