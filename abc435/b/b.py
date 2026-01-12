N = int(input())
A = list(map(int, input().split()))

# すべて約数でなければTrue
def is_divicor(num, A):
    for a in A:
        if num % a != 0:
            continue
        else:
            return False
    return True

cnt = 0
for l in range(N):
    for r in range(l+1, N):
        _sum = sum(A[l:r+1])
        if is_divicor(_sum, A[l:r+1]):
            cnt += 1
print(cnt)
