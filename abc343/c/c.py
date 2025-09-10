ans = []
for i in range(1000000):
    temp = pow(i,3)
    s_temp = str(temp)
    diff = reversed(s_temp)
    if s_temp == ''.join(diff):
        ans.append(temp)
N = int(input())
for a in reversed(ans):
    if N >= a:
        print(a)
        exit()
