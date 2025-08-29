MAX = 100000

def sieve(N):
    is_prime = [True] * (N+1)
    is_prime[:2] = [False] * 2
    for i in range(2, (N//2)+1):
        if not is_prime[i]:
            continue
        for j in range(i*i, N+1, i):
            is_prime[j] = False
    return is_prime

is_prime = sieve(MAX)

# (N + 1) / 2 で素数判定
A = [False] * (MAX+1)
for i in range(MAX+1):
    if not is_prime[i]:
        continue
    if is_prime[i] and is_prime[(i+1)//2]:
        A[i] = True

# 累積和
S = [0] * (MAX+1)
for i in range(MAX):
    S[i+1] = S[i] + A[i]

# 入力受け取り
# l - r
Q = int(input())
for q in range(Q):
    l, r = map(int, input().split())
    # l~r の累積和を求めたいから
    # S[r+1]-S[l]で求められる
    print(S[r+1]-S[l])
