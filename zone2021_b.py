N, D, H = list(map(int, input().split()))

max_stair = 0.0

for i in range(N):
    tmp_d, tmp_h = list(map(int, input().split()))
    tan = (H-tmp_h)/(D-tmp_d)
    h_dash = D*tan
    st = H - h_dash
    if st > max_stair:
        max_stair = st

print(max_stair)
