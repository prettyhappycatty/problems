

class train:
    prev = -1
    idx = -1
    next = -1

    def __init__(self, idx):
        self.idx = idx

    def set_next(self, idx):
        self.next = idx

    def set_prev(self, idx):
        self.prev = idx

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

N, Q = list(map(int, input().split()))

trains = [train(i) for i in range(N)]  

from collections import deque

for i in range(Q):
    query = list(map(int, input().split())) #string型list
    if query[0] == 1: #引数は3つ
        x = query[1]-1
        y = query[2]-1
        trains[x].set_next(y)
        trains[y].set_prev(x)
    elif query[0] == 2: #引数は3つ
        x = query[1]-1
        y = query[2]-1
        trains[x].set_next(-1)
        trains[y].set_prev(-1)
    else:#引数は2つ
        #for i in range(N):
        #    print(i, trains[i].get_prev(), trains[i].get_next())
        #print("query_x=", query[1])
        x = query[1]-1
        y = -1
        ans = deque([x+1])
        bef = deque()
        aft = deque()
        b = trains[x].get_prev()
        #print("query_start = ",x)
        while b != -1:#先頭までの間操作
            ans.appendleft(b+1)
            bef.appendleft(b+1)
            b = trains[b].get_prev()

        a = trains[x].get_next()
        while a != -1:#先頭までの間操作
            ans.append(a+1)
            aft.append(a+1)
            a = trains[a].get_next()

        print(len(ans), *list(ans))
        #print(len(ans), bef, x, aft)


        
