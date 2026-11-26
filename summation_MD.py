x = list(map(float, input().split()))
total = len(x)
result = 0
sum = 0

for i in x:
    result += i

avg = result / total

for i in x:
    z = abs(i - avg)
    sum += z

md = sum / total
print(avg)
print(md)