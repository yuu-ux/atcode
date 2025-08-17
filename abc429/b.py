Q = int(input())
box = []
for i in range(Q):
    query = list(input().split())
    if query[0] == '1':
        box.append(int(query[1]))
    elif query[0] == '2':
        print(box.pop(box.index(min(box))))
