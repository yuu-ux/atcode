A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = sum(A) - sum(B)
print(diff + 1)

