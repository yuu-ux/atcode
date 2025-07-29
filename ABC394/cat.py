N = int(input())
S = []
for i in range(N):
    S.append(input())

sorted_S = sorted(S, key=lambda x: len(x))
print(*sorted_S, sep='')
