
# T = int(input())
# cases = {}
# for _ in range(T):
#     N = int(input())
#     S = list(map(int, input().split()))
#     cases[N] = S
#

# for domi_num, domi in cases.items():
#     if search_domino := sorted_domino(domi_num, domi):
#         index = bisect.bisect_left(search_domino, domi[0] * 2)
#         domi[index] * 2
#     else:
#         print(-1)
#         break
import bisect
def sorted_domino(domi):
    if len(domi) == 2:
        return None
    return sorted(domi[1:-1])

T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    first = S[0]
    last = S[-1]

    ans = 2
    domino = first
    if dominos := sorted_domino(S):
        while domino * 2 < last:
            idx = bisect.bisect_right(dominos, domino * 2)
            if idx == 0:
                break
            elif idx == len(dominos):
                next = dominos[-1]
                if domino < next:
                    domino = next
                    ans += 1
                break
            else:
                next = dominos[idx - 1]
                domino = next
                ans += 1
    print(ans if domino * 2 >= last else -1)
