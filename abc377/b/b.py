def check_row(j):
    for k in range(8):
        if field[k][j] == '#':
            return False
    return True

def check_column(i):
    for k in range(8):
        if field[i][k] == '#':
            return True
    return False

field = []
res = 0
for _ in range(8):
    field.append(list(input()))
for i in range(8):
    for j in range(8):
        if check_column(i):
            break
        if check_row(j):
            res += 1
print(res)
