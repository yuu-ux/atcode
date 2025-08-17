N, L, R = map(int, input().split())
S = input()
for s in S[L-1:R]:
    if 'o' != s:
        print('No')
        exit()
print('Yes')
