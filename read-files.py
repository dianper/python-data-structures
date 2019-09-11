fname = input('Enter the file name: ')

# line by line
try:
    xfile = open(fname)
except:
    print('The file cannot be opened', fname)
    quit()

count = 0
for line in xfile:    
    print(line.rstrip())
    count = count + 1

print('count:', count)

# whole file
xfile = open(fname)
inp = xfile.read()
print(inp)