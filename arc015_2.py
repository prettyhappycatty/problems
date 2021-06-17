N = int(input())

mousho = 0
manatsu = 0
natsu = 0
nettai_ya = 0
fuyu = 0
mafuyu = 0


for i in range(N):
    MT_t, mT_t = map(float, input().split())
    if MT_t >= 35:
        mousho += 1
    elif MT_t >= 30:
        manatsu += 1
    elif MT_t >= 25:
        natsu += 1

    if mT_t >= 25:
        nettai_ya += 1

    if mT_t < 0 and MT_t >= 0:
        fuyu += 1
    if MT_t < 0:
        mafuyu += 1

print(mousho, manatsu, natsu, nettai_ya, fuyu, mafuyu)