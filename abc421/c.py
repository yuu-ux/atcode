N=int(input())
S=input()

x=[i for i, c in enumerate(S) if c == 'A']
y1 = [i*2 for i in range(2*N)]
y2 = [(i*2)+1 for i in range(2*N)]

ans1 = sum(abs(y1[j] - x[j]) for j in range(N))
ans2 = sum(abs(y2[j] - x[j]) for j in range(N))

print(min(ans1, ans2))
