f = open('3a.txt')
contrV = int(f.readline())
n = int(f.readline())
R = L = 0
summ = 0
now = []
ans = 0

for i in range(n):
    x = int(f.readline())
    now.append(x)
    summ += x
    R += 1
    if summ > contrV:
        while summ > contrV:
            L += 1
            summ -= now[0]
            now.pop(0)
    if summ == contrV:
        ans = max(R - L, ans)
f.close()

print(ans)
