H, W, C, Q = map(int, input().split())

TT, NN, CC = [], [], []
for i in range(Q):
    tt, nt, ct = map(int, input().split())
    TT.append(tt)
    NN.append(nt-1)
    CC.append(ct-1)

ans = [0 for i in range(C)]
done_1 = set()
done_2 = set()
for i in range(Q-1,-1,-1):
  if TT[i] == 1 and NN[i] not in done_1:
    done_1.add(NN[i])
    ans[CC[i]] += W - len(done_2)
  if TT[i] == 2 and NN[i] not in done_2:
    done_2.add(NN[i])
    ans[CC[i]] += H - len(done_1)

print(*ans)
