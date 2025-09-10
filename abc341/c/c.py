H, W, N = map(int, input().split())
T = input()
grid = [list(input()) for _ in range(H)]

cnt = 0
for i in range(1, H):
    for j in range(1, W):
        if grid[i][j] == '#':
            continue
        x,y = i, j
        for k in range(N):
            if T[k] == 'U':
                x -= 1
            elif T[k] == 'D':
                x += 1
            elif T[k] == 'L':
                y -= 1
            elif T[k] == 'R':
                y += 1
            if grid[x][y] == '#':
                break
        else:
            cnt += 1
print(cnt)
