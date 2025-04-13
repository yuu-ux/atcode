# 作り直し WC
# n, k = map(int, input().split())
#
# A = [1] * (n + 1)
# _sum = k * 2
# div = 1000000000
# if n < k:
#     print(1)
#     exit(0)
#
# # 1, 1, 2, 3, 5
# for i in range(k+1, n + 1):
#     A[i] = (_sum - A[i - k - 1]) % div
#     _sum += (A[i] - A[i - k -1]) % div
# print(A[n])

# AC
N, K = map(int, input().split())

MOD = 10**9

A = [0] * (N + 1)
cum = [0] * (N + 2)  # 累積和（cum[i] = A[0] + ... + A[i-1]）

for i in range(N + 1):
    if i < K:
        A[i] = 1
    else:
        A[i] = (cum[i] - cum[i - K]) % MOD
    cum[i + 1] = (cum[i] + A[i]) % MOD

print(A[N])

