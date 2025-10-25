import numpy as np

def calc_kyori(zahyou, zahyou1):
    differences = zahyou - zahyou1
    distances = np.linalg.norm(differences, axis=1)
    return sum(distances)

def move_elm(zahyou, zahyou1, kyori):
    for i in range(8):
    # 8方向に移動する
    # 距離を計算する
    # kyori と比較する
    # kyroiが短ければ更新する
    return 1

N = int(input())
zahyou = []
cnt = 0
_max = 0
for _ in range(N):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    if _max < max(x, y):
        _max = max(x, y)
    zahyou.append([x,y])
# _max * _max の平面である

np_zahyou = np.array(zahyou)
kyori = -1
while kyori != 0:
    for i in range(N):
        # 距離を測る
        kyori = calc_kyori(np_zahyou, np_zahyou[i])
        # 現在の距離よりも近くなる位置にコマを配置する
        # コマを移動
        move_elm(np_zahyou, np_zahyou[i], kyori)
    cnt += 1
print(cnt)
