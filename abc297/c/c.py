H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W-1):
        if S[i][j] == 'T' and S[i][j+1] == 'T':
            S[i][j] = 'P'
            S[i][j+1] = 'C'
# ans = [''.join(s) for s in S]
# print('\n'.join(ans))
# print('\n'.join(map(''.join, S)))
print(*(''.join(s) for s in S), sep='\n')
