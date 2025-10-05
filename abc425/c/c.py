def build_prefix(arr):
    """区間の求め方: S[r]-S[l-1]"""
    prefix = [0] * (len(arr) + 1)
    for i, v in enumerate(arr, start=1):
        prefix[i] = prefix[i - 1] + v
    return prefix

N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = A + A
prefix = build_prefix(B)
c = 0
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c = (c + query[1]) % N
        continue
    l, r = query[1], query[2]
    print(prefix[r+c] - prefix[l + c - 1])
