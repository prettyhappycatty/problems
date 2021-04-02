N, M = list(map(int, input().split()))

_dict = {}

for i in range(M):
    tmp = list(map(int, input().split()))
    #print(tmp)
    #print(_dict)
    if (tmp[0]-1) in _dict.keys():
        #print('yes')
        _dict[(tmp[0]-1)] += 1
    else:
        #print('no')
        _dict[(tmp[0]-1)] = 1

    if (tmp[1]-1) in _dict.keys():
        #print('yes')
        _dict[(tmp[1]-1)] += 1
    else:
        #print('no')
        _dict[(tmp[1]-1)] = 1

#print(_dict)

for i in range(N):
    if i in _dict.keys():
        print(_dict[i])
    else:
        print(0)