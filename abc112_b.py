N, T = map(int, input().split())

m_c = 1001
for i in range(N): 
    c, t = map(int, input().split())
    if t <= T:
        m_c = min(m_c, c)

if m_c == 1001:
    print("TLE")
else:
    print(m_c)