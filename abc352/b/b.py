S = list(input())
T = input()
t_len = len(T)

ans = []
cnt = 0
for i in range(t_len):
    if T[i] == S[cnt]:
        cnt += 1
        ans.append(i+1)
print(*ans)
