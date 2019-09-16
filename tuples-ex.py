hand = open('clown.txt')
di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        #retrieve/create/update
        di[w] = di.get(w, 0) + 1       

#print(di)

tmp = list()
for k,v in di.items():
    newt = (v,k)
    tmp.append(newt)

#print('Flipped', newt)

tmp = sorted(tmp, reverse=True)
#print('Sorted', tmp[:5]) #top 5

for v,k in tmp[:5]:
    print(k,v)