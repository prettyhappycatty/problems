N, X = map(int, input().split())

m_sum = 0
m_min = 10**3
for i in range(N):
    m_tmp = int(input())
    m_sum += m_tmp
    m_min = min(m_min, m_tmp)

X_ = X - m_sum
cnt = X_ // m_min + N
print(cnt)


