(y, x) = ('car', 'motorcycle')
print(x)

nums = (1, 2, 3, 4, 7, 8, 18, 13)
print(max(nums))

di = dict()
di['car'] = 2
di['motorcycle'] = 1

#tuples
for k,v in di.items() :
    print(k,v)

tups = di.items()
print(tups)

d = { 'z': 4, 'k': 8, 'r': 7 }
d.items()
print('sorting list of tuples', sorted(d.items()))
print('sorting list of tuples (reverse)', sorted(d.items(), reverse=True))
