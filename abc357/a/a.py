N, M = map(int, input().split())
H = list(map(int, input().split()))

com = 0
for i in range(N):
    com += H[i]
    if com > M:
        print(i)
        exit()
    elif com == M:
        print(i+1)
        exit()
print(N)
