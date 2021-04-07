N = int(input())
l = []
dict_poll = {}

max_cnt = 0
for i in range(N):
    tmp = input()
    #l.append(tmp)
    if tmp in dict_poll.keys():
        dict_poll[tmp] += 1
    else:
        dict_poll[tmp] = 1
    if max_cnt < dict_poll[tmp]:
        max_cnt = dict_poll[tmp]

sorted_list = sorted(dict_poll.items(), key=lambda x: x[0])

for item in sorted_list:
    if max_cnt == item[1]:
        print(item[0])

