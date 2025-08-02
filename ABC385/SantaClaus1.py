H, W, X, Y = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = list(input())
cnt = 0
x,y = X - 1, Y - 1
for t in T:
    if t == 'U' and x > 1 and S[x-1][y] != '#':
        x -= 1
    elif t == 'D' and x < H - 2 and S[x+1][y] != '#':
        x += 1
    elif t == 'L' and y > 1 and S[x][y-1] != '#':
        y -= 1
    elif t == 'R' and y < W - 2 and S[x][y+1] != '#':
        y += 1
    else:
        continue
    if S[x][y] == '@':
        S[x][y] = '.'
        cnt += 1
print(x+1, y+1, cnt)
