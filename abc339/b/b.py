def print_grid(grid, H):
    for i in range(H):
        print(''.join(grid[i]))

H, W, N = map(int, input().split())
grid = [['.'] * W for _ in range(H)]
x, y = 0,0
direction_list = list('URDL')
i = 0
direction = direction_list[0]
for _ in range(N):
    # 向きの更新と現在ますの書き換え
    if grid[y][x] == '.':
        i += 1
        direction = direction_list[i%4]
        grid[y][x] = '#'
    elif grid[y][x] == '#':
        i -= 1
        direction = direction_list[i%4]
        grid[y][x] = '.'

    # 移動
    if direction == 'U':
        y = (y - 1) % H
    elif direction == 'R':
        x = (x + 1) % W
    elif direction == 'D':
        y = (y + 1) % H
    elif direction == 'L':
        x = (x - 1) % W
print_grid(grid, H)
