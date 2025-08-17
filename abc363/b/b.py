N, T, P = map(int, input().split())
L = list(map(int, input().split()))

def count_up(L):
    for i in range(len(L)):
        L[i] += 1
    return L

ans = 0
while sum((l >= T for l in L)) < P:
    L = count_up(L)
    ans += 1
print(ans)
