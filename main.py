def add_new(ls, sum):
    new_ls = []
    i = 0
    while i < len(ls) and ls[i] > sum:
        new_ls.append(ls[i])
        i += 1
    new_ls.append(sum)
    while i < len(ls):
        new_ls.append(ls[i])
        i += 1
    return new_ls



n = int(input())
ls = list(map(int, input().split()))

ls.sort(reverse=True)

cost = 0
while len(ls) > 1:
    print(ls)
    x = ls.pop()
    y = ls.pop()
    sum = x + y
    cost += sum
    ls = add_new(ls, sum)

print(cost)