N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for b in B:
    if b in A:
        A.remove(b)
print(*A)
