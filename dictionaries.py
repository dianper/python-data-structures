mydict = dict()
mydict['key1'] = 10
mydict['key2'] = 20
mydict['key3'] = 30
print(mydict)
print(mydict['key2'])

mydict['key3'] = mydict['key3'] + 10
print(mydict)

print('key4' in mydict)

# counts
counts = dict()
names = ['name1', 'name2', 'name3', 'name1', 'name1', 'name4', 'name5', 'name5']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

x = counts.get('name6', 0)
print(x)

# counts simplified
newcount = dict()
for name in names:
    newcount[name] = newcount.get(name, 0) + 1
print(newcount)

# counts by input
wdict = dict()
line = input('write something..:')
words = line.split()

for word in words:
    wdict[word] = wdict.get(word, 0) + 1
print(wdict)

for key in wdict:
    print(key, wdict[key])

jjj = { 'key1': 1, 'key2': 2 }
print('list', list(jjj))
print('keys', jjj.keys())
print('values', jjj.values())
print('items', jjj.items()) #tuple

for a,b in jjj.items():
    print(a,b)

