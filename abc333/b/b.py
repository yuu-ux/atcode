S = input()
T = input()

# S_1とS_2が隣り合ってるか判定
# T_1とT_2が隣り合ってるか判定
# 両方隣り合ってれば Yes を出力
# 両方隣り合ってなければ Yes を出力
# それ以外は No を出力

pattern = ['A', 'B', 'C', 'D', 'E']
S1_index = pattern.index(S[0])
S2_index = pattern.index(S[1])
T1_index = pattern.index(T[0])
T2_index = pattern.index(T[1])
S_is_next = False
T_is_next = False

if (S1_index + 1) % 5 == S2_index or (S1_index - 1) % 5 == S2_index:
    S_is_next = True

if (T1_index + 1) % 5 == T2_index or (T1_index - 1) % 5 == T2_index:
    T_is_next = True

if S_is_next == T_is_next:
    print('Yes')
else:
    print('No')
