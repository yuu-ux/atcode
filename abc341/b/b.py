N = int(input())
A = list(map(int, input().split()))
case = [list(map(int, input().split())) for _ in range(N-1)]

for i in range(N-1):
    s, t = case[i]
    div = A[i] // s
    A[i+1] += (t * div)
print(A[N-1])
