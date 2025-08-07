N, D = map(int, input().split())
S = input()

cnt = 0
for s in S:
    if s == '@':
        cnt += 1

print(N - cnt + D)
