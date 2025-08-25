N, M = map(int, input().split())
table = {}
for _ in range(M):
    a, b = input().split()
    if b == 'F':
        print('No')
        continue
    if a not in table.keys():
        print('Yes')
    else:
        print('No')
    table[a] = 1
