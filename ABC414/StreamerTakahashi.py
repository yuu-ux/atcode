N, L, R = map(int, input().split())
ans = 0
for i in range(N):
    is_x = False
    is_y = False
    x, y = map(int, input().split())
    if L >= x:
        is_x = True
    if R <= y:
        is_y = True

    if is_x and is_y:
        ans += 1
print(ans)
