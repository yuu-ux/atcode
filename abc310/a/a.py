N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

if P > min(A) + Q:
    print(min(A) + Q)
else:
    print(P)
