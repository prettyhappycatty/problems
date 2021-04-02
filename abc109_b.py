N = int(input())
_dict = {}

flg = 0
for i in range(N):
    W = input()
    s = W[0]
    e = W[len(W)-1]
    #print(W, s, e)
    if i > 0 and (s != bef_e or W in _dict):
        flg = 1
        break
    bef_e = e
    _dict[W] = 1

if flg == 0:
    print('Yes')
else:
    print('No')