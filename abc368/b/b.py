N = int(input())
A = list(map(int, input().split()))
cnt = 0

while len(A) > 1:
    A.sort(reverse=True)
    if len(A) > 0 and A[0] > 0:
        A[0] -= 1
    if len(A) > 0 and A[1] > 0:
        A[1] -= 1
    while 0 in A:
        A.remove(0)
    cnt += 1
print(cnt)
