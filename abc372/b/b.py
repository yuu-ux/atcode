M = int(input())
N = 0
A = []
while M > 0:
    mod = M % 3
    for j in range(mod):
        A.append(N)
    M //= 3
    N += 1
print(len(A))
print(*A)
