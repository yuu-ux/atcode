S = list(input())

s_len = len(S)
res = 0
x = 0
start = 0
end = 0
t_len = 0
for i in range(s_len):
    if S[i] == 't':
        x += 1
        start = i
        for j in range(i+1, s_len+1):
            if S[j] == 't':
                end = j
                t_len = end - start + 1
                temp = (x-2)/(t_len-2)
                if res < temp:
                    res = temp
                break

print(res)
