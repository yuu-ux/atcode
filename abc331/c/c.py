N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict
import bisect
from collections import deque
import itertools

sorted_a = sorted(A)
prefix = deque(itertools.accumulate(sorted_a))
prefix.appendleft(0)

max_a = max(A)
l = 0
dic = defaultdict(int)
set_a = set(sorted_a)
for a in set_a:
    if a == max_a:
        continue
    r = N
    l = bisect.bisect_right(sorted_a, a)
    dic[a] = prefix[r] - prefix[l]
ans = []
for a in A:
    ans.append(dic[a])
print(*ans)
