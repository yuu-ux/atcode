import bisect
N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))


sorted_h = sorted(H)
sorted_b = sorted(B)
res = 0
for i in range(min(N, M)):
    head = sorted_h[i]
    ok = bisect.bisect_left(sorted_b, head)
    if ok < M:
        res += 1
if res >= K:
    print('Yes')
else:
    print('No')

# H > B の場合、ロボットは倒れる
# パースを組み合わせてKたいロボットが作れるか判定する
# 単純にH, Bを全探索してH<=Bを満たすものの個数を数えればいい。
# しかし、それだとO(N^2)になるため、計算が間に合わない。それをどうにかO(N)まで落としたい
# H を基準にHより大きいBがあるのかどうかがO(1)で分かれば良い
