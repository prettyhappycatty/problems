S = input()
K = int(input())

dur = []#X
part = []#.
dur_id = -1
part_id = -1

bef = ""
for i in range(len(S)):
    if bef != S[i]:
        change = True
    else:
        change = False

    if change == True and S[i] == "X":
        dur.append(1)
        dur_id += 1
    elif change == False and S[i] == "X":
        dur[dur_id] += 1

    
    if change == True and S[i] == "." and dur_id >= 0:
        part.append(1)
        part_id += 1
    elif change == False and S[i] == "." and dur_id >= 0:
        part[part_id] += 1
    bef = S[i]

if len(dur) == 0:#が一つもないとき "...."みたいなケース
    #print(part)
    print(min(len(S),K))
    exit()
if len(part) == 0:#まとまりが1つしかないとき(全部#、もしくはサイドに.がある場合) "XXXX" or "...XXXX..."のケース
    ans = min(len(S),dur[0]+K)
    print(ans)
    exit()

if len(part) == len(dur):
    part = part[:-1]
#print(dur)
#print(part)

dur_rui = [0]
part_rui = [0]

dur_sum = 0
for i in range(len(dur)):
    dur_sum += dur[i]
    dur_rui.append(dur_sum)

part_sum = 0
for i in range(len(part)):
    part_sum += part[i]
    part_rui.append(part_sum)

#print("dur",dur_rui)#lenはdur+1となるX
#print("part",part_rui)#lenはpart+1となる.

#埋められるもので最大となるidxを探す
max_umemoji = 0
max_len = 0
idx_i = -1
idx_j = -1
for i in range(len(part_rui)-1):
    for j in range(1,len(part_rui)):
        #print(i, j, max_umemoji,part_rui[j]-part_rui[i])
        if max_umemoji <= part_rui[j]-part_rui[i] and max_len < dur_rui[j-1]-dur_rui[i] + K:
            idx_i = i
            idx_j = j
            max_umemoji = part_rui[j]-part_rui[i]
            max_len = dur_rui[j-1]-dur_rui[i]+ K
        #    print("yes")
print(max_len)






