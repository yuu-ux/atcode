N, Y = map(int, input().split())

# for x in range(N+1):
#     t = Y - 1000 * N - 9000 * x # 4000y == t
#     if t % 4000 != 0:
#         continue
#     y = t // 4000
#     z = N - x - y
#     if y >= 0 and z >= 0:
#         print(x,y,z)
#         exit()
# print(-1, -1, -1)

for x in range(N+1):
    for y in range(N+1):
        z = N - x - y
        if not (0 <= z <= N):
            continue
        if (10000 * x + 5000 * y + 1000 * z) == Y:
            print(x,y,z)
            exit()
print(-1,-1,-1)
