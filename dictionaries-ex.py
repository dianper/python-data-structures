hand = open('intro.txt')
di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        #retrieve/create/update
        di[w] = di.get(w, 0) + 1       

#print(di)

#get the most common word
largest = -1
theword = None
for k,v in di.items() :
    #print(k, v)
    if v > largest :
        largest = v
        theword = k

print('Done', theword, largest)