N = int(input())
S = list(input())

if N % 2 == 0:
    print('No')
    exit()

if S[((N + 1) // 2)-1] != '/':
    print('No')
    exit()

tail = int((N + 1) // 2 - 1)
if any([s != '1' for s in S[0:tail]]):
    print('No')
    exit()
head = int((N + 1) // 2 + 1)-1
if any([s != '2' for s in S[head:N]]):
    print('No')
    exit()
print('Yes')
