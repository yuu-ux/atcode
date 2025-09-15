N, K = map(int, input().split())
currnet_k = K
current_time = 0
wait = []
stores = []
for i in range(N):
    A, B, C = map(int, input().split())
    # 来店できなければwaitlistに入れる
    if not (C < currnet_k) or wait:
        wait.append((A, B, C))
        continue
    # 入店できる
    # 今の時間を更新する
    current_time += A
    for j in range(len(stores)):
        if stores[j][1] <= current_time:
            currnet_k += stores[j][2]
            stores.pop(j)
    stores.append((A,B,C))
    currnet_k -= C
    print(A)

# 来店時間をO(1)で求めたい
