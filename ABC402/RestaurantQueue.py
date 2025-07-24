Q = int(input())
wait = []
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        wait.append(query[1])
    elif query[0] == 2:
        print(wait.pop(0))
