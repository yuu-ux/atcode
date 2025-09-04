import math
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    x1 = A[i][0]
    y1 = A[i][1]
    _max = 0
    ans = 0
    for j in range(N):
        x2 = A[j][0]
        y2 = A[j][1]
        temp = math.sqrt(pow((x1 - x2), 2) + pow(y1 - y2, 2))
        if temp > _max:
            _max = temp
            ans = j+1
    print(ans)
