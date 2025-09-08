H, W = map(int, input().split())
S = [input() for _ in range(H)]

def is_black(S, i, j, H, W):
    k = 0
    if not i == 0:
        k = i - 1
    cnt = 0
    while k <= i+1:
        if k >= H:
            break
        l = 0
        while l < W:
            if abs(i - k) + abs(j - l) == 1 and S[k][l] == '#':
                cnt += 1
            l += 1
        k += 1
    if cnt == 2 or cnt == 4:
        return True
    return False

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            continue
        if not is_black(S, i, j, H, W):
            print('No')
            exit()
print('Yes')

