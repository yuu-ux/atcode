N = int(input())
A = list(map(int, input().split()))

def check_even(A):
    for a in A:
        if a % 2 != 0:
            return False
    return True

ans = 0
while check_even(A):
    # for i in range(N):
    #     A[i] //= 2
    A = list(map(lambda x: x//2, A))
    ans += 1
print(ans)
