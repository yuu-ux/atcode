N = int(input())
T = 0
user = []
for i in range(N):
    S, C = input().split()
    C = int(C)
    user.append(S)
    T += C
user.sort()
print(user[T % N])
