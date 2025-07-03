def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    field = [0] * N
    ans = 0

    if N == 1:
        for i in range(Q):
            print(0 if i & 1 else 1)
        return

    for a in A:
        field[a - 1] ^= 1
# 白白 -1
# 白黒 +0
# 黒黒 +0
# 黒白 +1
        if a == 1:
            if field[a - 1] == 1 and field[a] == 0:
                ans += 1
            elif field[a - 1] == 0 and field[a] == 0:
                ans -= 1

# 白白 -1
# 黒黒 +0
# 白黒 +1
        elif a == N:
            if field[a - 1] == 0 and field[a - 2] == 0:
                ans -= 1
            elif field[a - 1] == 1 and field[a - 2] == 0:
                ans += 1

# 白x白 +1
# 白x黒 +0
# 黒黒白 +0
# 黒白黒 +1
        elif field[a - 1] == 1 and field[a - 2] == field[a] == 0:
            ans += 1
        elif field[a - 1] == field[a - 2] == field[a] == 0:
            ans -= 1
        elif field[a - 1] == field[a - 2] == field[a] == 1:
            ans -= 1
        elif field[a - 1] == 0 and field[a - 2] == field[a] == 1:
            ans += 1

        print(ans)

if __name__ == '__main__':
    main()
