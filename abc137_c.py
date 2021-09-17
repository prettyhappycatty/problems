N = int(input())

ary = []

for i in range(N):
    cnt = {}
    s = input()
    for j in range(len(s)):
        if s[j] not in cnt.keys():
            cnt[s[j]] = 0
        cnt[s[j]] += 1

    sorted_cnt = sorted(cnt.items(), key=lambda x:x[0])
    sorted_str = ""
    for sc in sorted_cnt:
        sorted_str += sc[0]+str(sc[1])

    ary.append(sorted_str)

dic_anagram = {}
for a in ary:
    if a not in dic_anagram.keys():
        dic_anagram[a] = 0
    dic_anagram[a] += 1

#print(ary)
#print(dic_anagram)
mul = 0
for k,v in dic_anagram.items():
    mul += v*(v-1)//2
print(mul)
