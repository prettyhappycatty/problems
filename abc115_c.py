N, K = list(map(int, input().split()))
list_tree = []

for i in range(N):
    tmp = int(input())
    list_tree.append(tmp)

list_tree.sort()

#print(list_tree)

m_h = 1000000000
for i in range(len(list_tree)-K+1):
    #print(i, j)
    h = list_tree[i+K-1] - list_tree[i]
    #print( list_tree[i+1])
    if m_h > h:
        m_h = h

print(m_h)
