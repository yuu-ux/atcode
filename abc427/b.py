N = int(input())
def sum_digit(N):
    if N < 10:
        return N
    list_N = list(str(N))
    int_list_N = map(int, list_N)
    return sum(int_list_N)

A = [0] * (N+1)
A[0] = 1
ans = 0
for i in range(1, N+1):
    total = 0
    for j in range(i):
        total += sum_digit(A[j])
    A[i] = total
print(A[N])
