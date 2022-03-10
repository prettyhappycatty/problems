x1, y1, x2, y2 = map(int, input().split())

neigh = [[1,2], [2,1],[-1,2],[2,-1],[-2,1],[1,-2],[-1,-2],[-2,-1]]



neigh_list_1 = []
neigh_list_2 = []

for nei in neigh:
    neigh_list_1.append([x1+nei[0], y1+nei[1]])
    neigh_list_2.append([x2+nei[0], y2+nei[1]])

for ent1 in neigh_list_1:
    for ent2 in neigh_list_2:
        if ent1[0] == ent2[0] and ent1[1] == ent2[1]:
            print("Yes")
            exit()

print("No")