# 数列(Ai..A_N-1)を全部かける
# 愚直にやればN^2でできそうだけど、制約がN<=3*10^5だからN^2だとTLEになる
N = int(input())
A = list(map(int, input().split()))
total = 0
for i in range(N):
    total += A[i]

total2 = 0
for j in range(N):
    total2 += pow(A[j], 2)

print((pow(total,2) - total2) // 2)
