Q = int(input())

deck = [0] * Q
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        deck.insert(0, query[1])
    elif query[0] == 2:
        print(deck.pop(0))
