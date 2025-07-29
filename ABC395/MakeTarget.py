def insert_color(res, i, j, color):
    for _i in range(i, j+1):
        for _j in range(i, j+1):
            res[_i][_j] = color
    return res

def main():
    N = int(input())

    res = [['.'] * N for _ in range(N)]
    for i in range(1, N+1):
        j = N + 1 - i
        if i > j:
            continue
        elif i <= j:
            if i % 2 == 0:
                res = insert_color(res, i-1, j-1, '.')
            else:
                res = insert_color(res, i-1, j-1, '#')
    for r in res:
        print(*r, sep='')

if __name__ == '__main__':
    main()
