X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())
module_map = {i: False for i in range(len(W))}
for i in range(Q):
    P = int(input())
    p_index = P - 1
    if module_map[p_index] == False:
        X += W[p_index]
        module_map[p_index] = True
    else:
        X -= W[p_index]
        module_map[p_index] = False
    print(X)
