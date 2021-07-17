f = open('1b.txt')
n = int(f.readline())

first = 10 ** 10
last = 0

for i in range(n):
    x = int(f.readline())
    first = min(first, x)
    last = max(last, x)

d = (last - first) / (n - 1)
ans = first + (d - 1) * d

f.close

print(int(ans))    
