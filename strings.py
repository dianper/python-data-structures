fruit = 'banana'

# loop while
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# loop for
for letter in fruit:
    print(letter)

count = 0
for letter in fruit:
    if letter == 'a':
        count = count + 1
print(count)

# substring
name = 'Diego Pereira'
print(name[0:5])
print(name[1:5])

# ifs
if fruit == 'banana':
    print('All right, banana')

if fruit > 'banana':
    print('>')
elif fruit < 'banana':
    print('<')
else:
    print('All right, banana')

# lowercase
print('HI THERE'.lower())

# uppercase
print(fruit.upper())

# typeof
print(type(fruit))

# methods
print(dir(fruit))

# find (-1)
print(fruit.find('v'))

# find
print(fruit.find('a'))

# lstrip / rstrip / strip
# remove spaces
spacestring = '  Diego Pereira  '
print(spacestring.rstrip())
print(spacestring.lstrip())

data = 'From user.name@hostemail.com  Fri Set 9 21:00:00 2019'
atpos = data.find('@')
print(atpos)

sppos = data.find('  ')
print(sppos)

host = data[atpos+1 : sppos]
print(host)