N = int(input())

cur_x = 0
cur_y = 0
cur_t = 0
for _ in range(N):
    t, x, y = map(int, input().split())
    diff_x = abs(cur_x - x)
    diff_y = abs(cur_y - y)
    cur_t += diff_x + diff_y
    if cur_t > t or (cur_t < t and (t - cur_t) % 2 != 0):
        print('No')
        exit()
    cur_x = x
    cur_y = y
print('Yes')
