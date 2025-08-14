N = int(input())
left_hand = -1
right_hand = -1
ans = 0
for _ in range(N):
    A, S = input().split()
    a = int(A)
    if S == 'L':
        if left_hand == -1:
            left_hand = a
        else:
            ans += abs( (a - left_hand) )
            left_hand = a
    else:
        if right_hand == -1:
            right_hand = a
        else:
            ans += abs((a - right_hand))
            right_hand = a
print(ans)
