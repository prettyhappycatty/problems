s = input()

dic = {}
for i in range(len(s)):
    if s[i] not in dic.keys():
        dic[s[i]] = []
    dic[s[i]].append(i)


max_dur_list = []
for k,v in dic.items():
    pre = -1
    max_dur = 0
    for i in range(len(v)):
        dur=v[i]-pre
        max_dur = max(max_dur, dur)
        pre = v[i]
    dur = len(s)-pre
    max_dur = max(max_dur, dur)
    #print(k, max_dur)
    max_dur_list.append(max_dur)

print(min(max_dur_list)-1)