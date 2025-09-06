N, A, B = map(int, input().split())
week = A + B
D = sorted(int(x) % week for x in input().split())
D += [d + week for d in D[:N]]

for j in range(len(D)-1):
    if D[j+1] - D[j] >= B+1:
        print('Yes')
        break
else:
    print('No')
# E = sorted({d % week for d in D})
# k = len(E)
# for i in range(k):
#     diff = (E[(i+1)%k] - E[i]) % week
#     if diff > B:
#         print('Yes')
#         break
# else:
#     print('No')
#
