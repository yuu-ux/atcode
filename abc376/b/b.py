N, Q = map(int, input().split())
res = 0
L, R = 0, 1
# H is L or R
# T is target index
# s: R or L index
# t: target index
# b: R or L index
# N: N

def move_cost(s, t, b, N):
    if s == t:
        return 0
    d_cw  = (t - s) % N          # 時計回り距離
    d_ccw = (s - t) % N          # 反時計回り距離
    # b が s→t の時計回り弧に含まれるか？
    blocked_cw  = 0 < ((b - s) % N) <= d_cw
    # blocked_cw が真なら反時計回り、偽なら時計回りが唯一の合法方向
    return d_ccw if blocked_cw else d_cw

for _ in range(Q):
    H, T = input().split()
    t = int(T)-1
    if H == 'R':
        res += move_cost(R, t, L, N)
        R = t
    else:
        res += move_cost(L, t, R, N)
        L = t
print(res)
