N = int(input())
A = list(map(int, input().split()))
dict_a = {v:i+1 for i, v in enumerate(A)}
sorted_dict_a = dict(sorted(dict_a.items()))
res=''
i=0
for v in sorted_dict_a.values():
    if i == 2:
        print(v)
        break
    else:
        print(v, end=' ')
        i+=1

# N = int(input())
# A = list(map(int, input().split()))
#
# pos_by_value = {v: i + 1 for i, v in enumerate(A)}
# top3_positions = list(dict(sorted(pos_by_value.items())).values())[:3]
# print(*top3_positions)
