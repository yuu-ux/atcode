N = int(input())
S = input()
T = input()

res = 0
for i in range(N):
    if S[i] != T[i]:
        res += 1
print(res)
