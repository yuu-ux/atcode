N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

dic = {}
# O(N)
for i in range(N):
    if A[i] not in dic:
        dic[A[i]] = [W[i]]
    else:
        dic[A[i]].append(W[i])
ans = 0
for key, value in dic.items():
    # リストの長さをkとする
    # k - 1繰り返すので、O(k^2)
    if len(value) >= 2:
        # min O(k)
        # index O(k)
        # pop O(k)
        ans += sum(value) - max(value)
print(ans)

