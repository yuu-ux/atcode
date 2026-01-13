N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

def serarch_field(S, i, j):
    res = []
    for k in range(M):
        temp = ''
        for l in range(M):
            temp += S[i+k][j+l]
        res.append(temp)
    return res

res = set()
for i in range(N):
    if i + M > N:
        break
    temp = ""
    for j in range(N):
        if j + M > N:
            break
        res.add(tuple(serarch_field(S,i,j)))
print(len(list(res)))
# for s in S:
#     print(''.join(s))
