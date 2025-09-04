N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ans = {}
for i in range(N):
    color = A[i][1]
    tasty = A[i][0]
    if not color in ans:
        ans[color] = tasty
        continue
    if ans[color] > tasty:
        ans[color] = tasty
print(max(ans.values()))
