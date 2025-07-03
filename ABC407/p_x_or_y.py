X, Y = map(int, input().split())

def is_X(i, j, X):
    if (i + j) >= X:
        return True
    return False

def is_Y(i, j, Y):
    if abs(i - j) >= Y:
        return True
    return False

cnt = 0
for i in range(1, 7):
    for j in range(1, 7):
        if is_X(i, j, X) or is_Y(i, j, Y):
            cnt += 1
print(cnt / 36)



