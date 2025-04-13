nums = list(map(int, input().split()))
bk = [0] * 13
for i in range(7):
    x = nums[i]
    bk[x - 1] += 1

bk.sort(reverse=True)

if bk[0] >= 3 and bk[1] >= 2:
    print('Yes')
else:
    print('No')
