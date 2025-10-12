N, S, M, L = map(int, input().split())

ans = []
for i in range((100//6)+2):
    for j in range((100//8)+2):
        for k in range((100//12)+2):
            if N <= (i * 6) + (j * 8) + (k * 12):
                ans.append(i * S + j * M + k * L)
print(min(ans))

# S: 6
# M: 8
# L: 12
