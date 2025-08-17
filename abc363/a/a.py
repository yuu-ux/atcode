R = int(input())

ans = 0
if 1 <= R <= 99:
    ans = 100 - R
elif 100 <= R <= 199:
    ans = 200 - R
elif 200 <= R <= 299:
    ans = 300 - R
elif 300 <= R <= 399:
    ans = 400 - R
print(ans)
