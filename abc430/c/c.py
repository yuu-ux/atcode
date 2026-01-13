N, A, B = map(int, input().split())
S = list(input())

# O(N) で解きたい問題
a_cnt = 0
b_cnt = 0
for s in S:
    if s == 'a':
        a_cnt += 1
    if s == 'b':
        b_cnt += 1
print(a_cnt)
print(b_cnt)
