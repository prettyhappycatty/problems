import copy

N = int(input())

#3人入れる、総合スコアを計算する、次の人を入れ替えるか決める

member = []

def chks_core(member):
    large = [0, 0, 0, 0, 0]
    for i in range(3):
        for set_i in range(5):
            #print("i,seti", i, set_i)
            #print(smallest[set_i],member[i][set_i])
            if large[set_i] < member[i][set_i]:
                large[set_i] = member[i][set_i]
 
    sum_smallest = 10e9
    for i in range(len(large)):
        if sum_smallest > large[i]:
            sum_smallest = large[i]

    return sum_smallest, smallest


smallest = [10e9, 10e9, 10e9, 10e9, 10e9]
sm_score = 5*10e5
for i in range(N):
    tmp_a, tmp_b, tmp_c, tmp_d, tmp_e = list(map(int, input().split()))
    if i < 3:
        #print("c", len(member))
        member.append([tmp_a, tmp_b, tmp_c, tmp_d, tmp_e])
        if i == 2:
            sm_score, smallest = chks_core(member)
    else:
        #print("c", len(member))
        tmp_member = copy.copy(member)
        tmp_sm_score = sm_score
        tmp_smallest = smallest
        smallest_i = -1
        for j in range(3):#1人ずつ交換したときのスコアを確認、誰と交換するのがいいか？スコアが大きくなるよう
            tmp_member = copy.copy(member)
            tmp_member[j] = [tmp_a, tmp_b, tmp_c, tmp_d, tmp_e]
            t_sm_score, t_smallest = chks_core(tmp_member)
            print("change", tmp_member[j],[tmp_member[0], tmp_member[1],tmp_member[2]], i, j, t_sm_score, tmp_sm_score)
            if t_sm_score > tmp_sm_score:
                tmp_sm_score = t_sm_score
                tmp_smallest = t_smallest
                smallest_i = j
        if smallest_i > -1:
            member[smallest_i] = [tmp_a, tmp_b, tmp_c, tmp_d, tmp_e]  
            smallest = t_smallest
            sm_score = t_sm_score

print(sm_score)




