import random

# result = dir(random)
# result = help(random)
#
# result = random.random()*100

# result = int(random.uniform(10,100))
# result = random.randint(20,30)
# print(result)

names = ["Ömer","GND","2021"]
greeting = "Hello There"
result = names[random.randint(0,len(names)-1)]
result = random.choices(names) # listeden rastgele eleman çağırır
result = random.choices(greeting)
liste = list(range(10))
random.shuffle(liste) # Listeyi karıştırır
result = liste

liste = range(100)
result = random.sample(liste,3) # tanımladığımız liste içerisinden istediğimiz sayı kadar veri getirir
print(result)