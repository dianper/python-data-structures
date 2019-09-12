friends = ['f1', 'f2', 'f3']

for f in friends:
    print('happy new year ', f)
print('done!')

narray = [1, 2, 3, 4, 5]
narray[2] = 6
print(narray)

stuff = list()
print(stuff)

stuff.append('dog')
stuff.append('cat')
stuff.append('horse')

if 88 in stuff:
    print('exists')
else:
    print('not exists')

stuff.sort()
print(stuff)

nums = [1, 2, 3, 4, 5, 6]
print('sum', sum(nums))
print('avg:', sum(nums) / len(nums))
print('max:', max(nums))
print('min:', min(nums))

line = 'value1;value2;value3'
thing = line.split(';')
print(thing)
print(len(thing))

