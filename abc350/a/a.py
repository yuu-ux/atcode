S = list(input())
num = int(''.join(S[3:]))
if num == 316:
    print('No')
    exit()
if 0 < num < 350:
    print('Yes')
else:
    print('No')
