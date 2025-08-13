S = list(input())

def search_right(S, cur):
    i = S.index(cur)
    cnt = 0
    while i < 25:
        i += 1
        cnt += 1
        if S[i] == chr(ord(cur)+1):
            return cnt
    return 0

def search_left(S, cur):
    i = S.index(cur)
    cnt = 0
    while 0 < i:
        i -= 1
        cnt += 1
        if S[i] == chr(ord(cur)+1):
            return cnt
    return 0

ans = 0
current = 'A'
while current != chr(ord('Z')+1):
    ans += search_right(S, current)
    ans += search_left(S, current)
    current = chr(ord(current)+1)
print(ans)

