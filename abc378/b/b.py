N = int(input())
trash = [list(map(int,input().split())) for _ in range(N)]
Q = int(input())
query = [list(map(int,input().split())) for _ in range(Q)]

# for type, day in query:
#     div,rem = trash[type-1]
#     while day % div != rem:
#         day += 1
#     print(day)
for type, day in query:
    div, rem = trash[type - 1]
    offset = (rem - (day % div)) % div
    print(day + offset)
