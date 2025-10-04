x,y = input().split()
if x == 'Ocelot':
    nx = 0
elif x == 'Serval':
    nx = 1
else:
    nx = 2

if y == 'Ocelot':
    ny = 0
elif y == 'Serval':
    ny = 1
else:
    ny = 2

if nx >= ny:
    print('Yes')
else:
    print('No')

