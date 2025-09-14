N = int(input())
bars = set()
for _ in range(N):
    bar = input()
    bars.add(min(bar, bar[::-1]))
print(len(bars))
# 愚直にやると、
# 反転した文字列も合わせてbarsに追加していってsetする
# reverse に O(N) 必要だから、最悪(2*10^5)^2 になる
# 実行制限 2msec だから間に合わない
# bars の個数が答え
# N本の棒の中に何本異なる棒が存在するかを答える
# 棒の一致判定を工夫する必要がある
