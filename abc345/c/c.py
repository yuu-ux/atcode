from collections import defaultdict

S = input()
N = len(S)
ans = 0
# defaultdictを使うことで存在チェックが必要なくなる
count=defaultdict(int)
# 1 <= i < j <= N の j を走査する
for j in range(N):
    # j と同じ要素であれば入れ替えても新しい文字列は作れないため、マイナスする
    ans+=j-count[S[j]]
    # i を記録する
    count[S[j]] += 1
# 同じ文字の入れ替えによりSが作れるため、同じ要素が出てくる場合、1だけ加算する
if max(count.values()) > 1:
    ans+=1
print(ans)




# from collections import Counter
# S = input()
# N = len(S)
# counter_s = Counter(S)
# all_conb = (N*(N-1))//2
# duplicate = 0
# flg_dup = False
# for k,v in counter_s.items():
#     if v < 2:
#         continue
#     flg_dup = True
#     duplicate += (v*(v-1))//2
# if flg_dup:
#     print(all_conb - duplicate + 1)
# else:
#     print(all_conb + duplicate)
