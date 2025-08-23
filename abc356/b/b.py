# M種類の栄養素の目標値が設定されている
# それを各日で達成しているかどうかを確認する
# N, M
# A
# X..X_N

N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]

for i in range(M):
    total = 0
    for j in range(N):
        total += X[j][i]
    if A[i] > total:
        print('No')
        exit()
print('Yes')
