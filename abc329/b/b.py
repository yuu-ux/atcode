N = int(input())
A = set(map(int, input().split()))

max_a = max(A)
A.remove(max_a)
print(max(A))

