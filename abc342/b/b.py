N = int(input())
P = list(map(int, input().split()))
Q = int(input())
dict_P = {v:i for i, v in enumerate(P)}
for i in range(Q):
    A, B = map(int, input().split())
    if dict_P[A] < dict_P[B]:
        print(A)
    else:
        print(B)
