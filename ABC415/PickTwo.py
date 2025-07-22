S = list(input())

flg = True
for i,s in enumerate(S, 1):
    if s == '#':
        print(i, end='')
        if flg:
            print(',', end='')
            flg = False
        else:
            print('')
            flg = True

