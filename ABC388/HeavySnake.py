N, D = map(int, input().split())

snake = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, D+1):
    _max = 0
    for j in range(N):
        temp = snake[j][0] * (snake[j][1] + i)
        if temp > _max:
            _max = temp
    print(_max)
