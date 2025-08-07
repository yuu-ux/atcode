N, A, B = map(int, input().split())
S = input()

if A == 0 and B == 0:
    print(S)
elif B == 0:
    print(S[A:])
else:
    print(S[A:-B])
