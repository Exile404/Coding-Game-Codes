c = int(input())
items = sorted(map(int, input().split()))
count = sum(1 for i in range(len(items)) if sum(items[:i+1]) <= c)
print(count)
