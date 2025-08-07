import math

# 5, 6
N, L = map(int, input().split())
D = list(map(int, input().split()))

ratio = L / 3
if not ratio.is_integer():
    print(0)
    exit()
circle = {i: 0 for i in range(L)}
circle[0] = 1

current = 0
for d in D:
    circle[(current + d) % L] += 1
    current = (current + d) % L
cnt = 0
for i in range(L):
    if circle[i] == 0:
        continue
    if circle[i] >= 1:
        ratio = L // 3
        if circle[ratio] >= 1 and circle[ratio + ratio] >= 1:
            condition = circle[i] + circle[ratio] + circle[ratio + ratio]
            print(condition)
            cnt = math.comb(condition, 3)
print(cnt)
# [4 3 1 2]
# {1: 1, 2: 1, 3: 0, 4: 2, 5: 0, 6: 0}
# 1, 2, 4
