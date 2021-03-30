w = input()
w_dict = {}

for s in w:
    if s in w_dict.keys():
        w_dict[s] += 1
    else:
        w_dict[s] = 1

flg = 0
for s in w_dict.keys():
    if w_dict[s] % 2 != 0:
        flg = 1
        break

if flg == 0:
    print('Yes')
else:
    print('No')