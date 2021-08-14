#typical90_003 DFSとBFS　dfs

import sys, copy

sys.setrecursionlimit(10000000)

N= int(input())#N個の都市


class Node:
    def __init__(self, data):
        self.neighbors = []
        self.data = data
        self.dist = -1

nodes = [Node(i) for i in range(N)]

def connect(a, b):
    nodes[a-1].neighbors.append(b-1)
    nodes[b-1].neighbors.append(a-1)


def print_nodes(nodes):
    for i in range(len(nodes)):
        print(nodes[i].data, nodes[i].neighbors, nodes[i].dist)


for i in range(N-1):
    tmpA, tmpB = map(int, input().split())
    connect(tmpA, tmpB)

nodes2 = copy.deepcopy(nodes)

# dfs
def dfs(v, dist, nodes):
    if nodes[v].dist > -1 : return nodes[v].dist, v  # 同じ頂点を2度以上調べないためのreturn
    nodes[v].dist = dist #到達した都市をTrueにする
    #print("d", dist, nodes[v-1].dist)
    #print("n",nodes[v-1].neighbors)
    maxdist = 0
    maxid = -1
    for vv in nodes[v].neighbors:
    #     print(dist)
        tmpdist, tmpid = dfs(vv, dist+1, nodes)
        if nodes[vv].dist < nodes[v].dist:
            continue
        if tmpdist > maxdist:
            maxdist = tmpdist
            maxid = tmpid
    return maxdist, maxid 


maxdist, maxid = dfs(1, 0, nodes)
mlen = 0
mlenid = -1
for i in range(N):
    if mlen < nodes[i].dist:
        mlen = nodes[i].dist
        mlenid = i

maxdist, maxid = dfs(mlenid, 0, nodes2)

mlen = 0
for i in range(N):
    if mlen < nodes2[i].dist:
        mlen = nodes2[i].dist

print(mlen+1)
#print_nodes(nodes)