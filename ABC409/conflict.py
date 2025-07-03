N = int(input())
T = input()
A = input()

ans = ''
for i in range(N):
    if T[i] == A[i] == 'o':
        ans = 'Yes'
        break
    else:
        ans = 'No'
print(ans)
