N = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(N):
    ans.append(A[i])
    if len(ans) < 2:
        continue
    if ans[-1] != ans[-2]:
        continue
    while ans[-1] == ans[-2]:
        ans.pop(-1)
        temp = ans.pop(-1)
        ans.append(temp + 1)
        if len(ans) < 2:
            break
print(len(ans))
