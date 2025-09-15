N, R = map(int, input().split())
L = list(map(int, input().split()))

if all(l for l in L):
    print(0)
    exit()

ans = 0
left_start = 0
right_start = N-1

for i in range(N):
    if L[i] == 0:
        left_start = i
        break

for i in range(N-1, -1, -1):
    if L[i] == 0:
        right_start = i
        break

for i in range(R, right_start+1):
    if L[i] == 0:
        ans += 1
    elif L[i] == 1:
        ans += 2

for i in range(R-1, left_start-1, -1):
    if L[i] == 0:
        ans += 1
    elif L[i] == 1:
        ans += 2
print(ans)
