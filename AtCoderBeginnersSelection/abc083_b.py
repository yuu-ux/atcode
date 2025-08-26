N, A, B = map(int, input().split())

def cumulative(N, ans):
    if N == 0:
        return ans
    return cumulative(N // 10, ans + N % 10)
    # return sum(int(c) for c in str(N))

ans = []
for i in range(1, N+1):
    temp = cumulative(i, 0)
    if temp >= A and temp <= B:
        ans.append(i)
print(sum(ans))
