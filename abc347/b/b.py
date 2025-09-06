S = input()
N = len(S)

ans = []
for i in range(N):
    temp = S[i]
    for j in range(i+1, N):
        temp += S[j]
        ans.append(temp)
for s in S:
    ans.append(s)
print(len(set(ans)))
