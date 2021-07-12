N, C = map(int, input().split())

days = []
start_days = []
end_days = []

events = []

for i in range(N):
  start_day, end_day, cost= map(int, input().split())
  events.append((start_day-1, cost))
  events.append((end_day, -cost))
    
events_sort = sorted(events, key=lambda x:x[0])
#print(events_sort)

ans = 0
fee = 0
t = 0
for x, y in events_sort:
    if x != t:
        ans += min(C, fee) * (x - t)
        t = x
    fee += y

print(ans)