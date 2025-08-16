H, W = map(int, input().split())
x, y = map(int, input().split())
S = [list(input()) for _ in range(H)]
query = list(input())

x -= 1
y -= 1
for q in query:
    if q == 'U' and x > 0 and S[x-1][y] == '.':
        x -= 1
    elif q == 'D' and x < H-1 and S[x+1][y] == '.':
        x += 1
    elif q == 'L' and y > 0 and S[x][y-1] == '.':
        y -= 1
    elif q == 'R' and y < W-1 and S[x][y+1] == '.':
        y += 1
print(x+1, y+1)
