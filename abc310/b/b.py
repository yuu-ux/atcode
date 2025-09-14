N, M = map(int, input().split())
product = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    P_i = product[i][0]
    C_i = product[i][1:]
    for j in range(N):
        P_j = product[j][0]
        C_j = product[j][1:]
        if not (P_i >= P_j):
            continue
        if not (all(c_i in C_j[1:] for c_i in C_i[1:])):
            continue
        if not (P_i > P_j or any(c_j not in C_i[1:] for c_j in C_j[1:])):
            continue
        print('Yes')
        exit()
print('No')
