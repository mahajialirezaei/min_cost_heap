import heapq

n = int(input())
ls = list(map(int, input().split()))

heapq.heapify(ls)

cost = 0
while len(ls) > 1:
    x = heapq.heappop(ls)
    y = heapq.heappop(ls)
    sum = x + y
    cost += sum
    heapq.heappush(ls, sum)

print(cost)