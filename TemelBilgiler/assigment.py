# x = 10
# y = 20
# z = 30

# x,y,z = 1, 3 ,5
# x,y = y,x

# x = x + 5
# x += 5

# x = x - 5
# x -= 5

# x = x * 5
# x *= 5

# x = x / 5
# x /= 5

# x = x % 5
# x %= 5

# x = x // 5
# x //= 5

# x = x ** 5
# x **= 5
# print(x, y, z)

values = 1,2,3,4,5
print(values)
print(type(values))

x,y,*z =values
print(x,y,z[0])
