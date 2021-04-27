N, M = list(map(int, input().split()))

st = []
cp = []
for i in range(N):
    tmp_a, tmp_b = list(map(int, input().split()))
    st.append((tmp_a, tmp_b))

for j in range(M):
    tmp_c, tmp_d = list(map(int, input().split()))
    cp.append((tmp_c, tmp_d))

#print(st)
#print(cp)

shortest = {}
shortest_id = {}

def getManhDist(st_set, cp_set):
    return abs(st_set[0]-cp_set[0])+abs(st_set[1]-cp_set[1])

for i in range(N):
    for j in range(M):
        manhdist = getManhDist(st[i], cp[j])

        if i not in shortest.keys():
            shortest[i] = 10e8 * 2

        if shortest[i] > manhdist:
            shortest[i] = manhdist
            shortest_id[i] = j


#print(shortest_id)
for key,item in shortest_id.items():
    print(item+1)