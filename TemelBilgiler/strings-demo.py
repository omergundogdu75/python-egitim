website = "http://www.google.com"
course =" Python Kursu baştan sona programlama"

length = len(website)
# print(result)

# result = website[7:10]
result = website[length-3:length]

result = course[:15]
result = course[-15:]
result = course[::] # bütün ifadeyi yazdırır
result = course[::2]
result = course[::-1] #tersten yazdırma
result = "12345"*5
result = result[::5]

name, surnname , age, job  = "ÖMER","GÜNDOĞDU",27,"Mekatronik Mühendisi"
result = f"Benim Adım {name} {surnname}, yaşım {age} ve mesleğim {job}"

result = "Hello World"
result = result.replace("W","w")

result ="abc"*3

print(result)