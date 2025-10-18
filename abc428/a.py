S, A, B, X = map(int, input().split())
ans = 0
while X > 0:
    if X > A:
        ans += S * A
        X -= A
    else:
        ans += S * X
        X = 0
    X -= B
print(ans)
