N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    ans += a
    if ans < 0:
        ans = 0
print(ans)
