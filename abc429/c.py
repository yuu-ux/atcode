# 愚直にやるとO(N^3)になるから、O(N)まで落としたい
# iから右側に同じ数がいくつあるのか。
# i自身が同じ数であるのか
# n=3で全て値が一致するケースを除き、A_iの要素が2個以上ある場合、0<ansになる
# 逆に同じ数でない数の個数を数える
from collections import Counter
N = int(input())
A = list(map(int, input().split()))

# counter_a = Counter(A)

ans = 0
for i in range(N):
    cnt = 0
    for j in range(1, N):
        for k in range(2, N):
            counter_a = Counter([A[i], A[j], A[k]])
            print(counter_a)
    if cnt == 2:
        ans += 1
print(ans)
