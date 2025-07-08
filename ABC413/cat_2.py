N = int(input())
S = []
for _ in range(N):
    S.append(input())

ans = set()
for i in range(N):
    for j in range(N):
        if i != j:
            ans.add(S[i] + S[j])
print(len(ans))
