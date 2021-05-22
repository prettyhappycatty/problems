S = input()

change_dic = {'0':'0','1':'1','6':'9','8':'8','9':'6'}

s_rev = list(reversed(S))
#print(s_rev)

ret = []
for st in s_rev:
    ret.append(change_dic[st])

print(''.join(ret))