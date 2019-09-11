str = 'Diego Pereira: 28'
ipos = str.find(':')
piece = str[ipos+2:]
value = float(piece) + 2
print(value)