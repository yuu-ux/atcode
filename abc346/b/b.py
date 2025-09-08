t = "wbwbwwbwbwbw"
W, B = map(int, input().split())

for i in range(12):
    w = b = 0
    for j in range(W + B):
        if t[(i + j) % 12] == 'w':
            w += 1
        else:
            b += 1
    if w == W and b == B:
        print('Yes')
        break
else:
    print('No')
