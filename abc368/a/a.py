N, K = map(int,input().split())
A = list(map(int, input().split()))

tail = A[-K:]
print(*(tail + A[:-K]))
