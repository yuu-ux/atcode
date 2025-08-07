N, D = map(int, input().split())
S = list(input())

for i in range(1, N+1):
    if D == 0:
        break
    if S[N - i] == '@':
        S[N - i] = '.'
        D -= 1
print(*S, sep='')
