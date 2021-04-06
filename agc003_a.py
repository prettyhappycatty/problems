S = input()

N_c = S.count('N')
E_c = S.count('E')
W_c = S.count('W')
S_c = S.count('S')

flg_NS = 0
flg_EW = 0

if N_c == S_c == 0 or (N_c > 0 and S_c > 0):
    flg_NS = 1

if E_c == W_c == 0 or (E_c > 0 and W_c > 0):
    flg_EW = 1

if flg_EW * flg_NS == 1:
    print('Yes')
else:
    print('No')


