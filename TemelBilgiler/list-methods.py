numbers = [ 2,4,1,3,5,8,9,7,6,7]
letters = ["g","b","c","d","e","f","a"]
# val = min(numbers)
# val = max(numbers)
# val = min(letters)
# val = max(letters)
# val = numbers[3:]
# val = numbers[:4]
# numbers[4] = 10
# print(numbers)

# numbers.append(49) # ensona ekler
# numbers.insert(3,78) # belirtilen indexe 78i ekler
# numbers.pop() # ensondaki eleman silinir
# numbers.pop(1)
# numbers.remove(7)
numbers.sort()
letters.sort()

numbers.reverse()
letters.reverse()

print(letters)
print(numbers)

print(len(numbers))
print(len(letters))

print(numbers.count(7))
print(letters.count("a"))

numbers.clear()
print(numbers)