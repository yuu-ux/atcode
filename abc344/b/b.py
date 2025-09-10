ans = []
for _ in range(100):
    try:
        ans.append(input())
    except:
        break
for a in reversed(ans):
    print(a)
