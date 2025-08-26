import math

N = int(input())
A = list(map(int, input().split()))

alice = []
bob = []
for i in range(math.ceil(N/2)):
    alice.append(A.pop(A.index(max(A))))
    if A:
        bob.append(A.pop(A.index(max(A))))
print(sum(alice) - sum(bob))
