N = int(input())
S = [input() for _ in range(N)]
before = S[0]
for i in range(1, N-1):
    if before == S[i] == 'sweet':
        print('No')
        exit()
    before = S[i]
print('Yes')
