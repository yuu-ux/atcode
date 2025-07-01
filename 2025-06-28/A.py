day = int(input())
tasks = []
for _ in range(day):
    pre, done = map(int, input().split())
    tasks.append((pre, done))

cnt = 0
for goal, result in tasks:
    if goal < result:
        cnt += 1

print(cnt)
