f = open('6b.txt')
n = int(f.readline())

b = 10**20
ans = [b] * 16
rez = [b] * 16

a = f.readline().split()
for i in range(len(a)):
    a[i] = int(a[i])
a.sort()
for i in range(3):
    for j in range(i+1, 3):
        ans[(a[i] + a[j]) % 16] = a[i] + a[j]
for i in range(n - 1):
    x,y,z = map(int, f.readline().split())
    for j in range(len(ans)):
        if ans[j] != 0:
            if (ans[j] + x +y) < rez[(ans[j] + x + y) % 16]:
                rez[(ans[j] + x + y) % 16] = (ans[j] + x + y)
            if (ans[j] + x + z) < rez[(ans[j] + x + z) % 16]:
                rez[(ans[j] + x + z) % 16] = (ans[j] + x + z)
            if (ans[j] + y + z) < rez[(ans[j] + y + z) % 16]:
                rez[(ans[j] + y +z) % 16] = (ans[j] + y + z)
    for j in range(len(ans)):
        ans[j] = rez[j]
        rez[j] = b
        
print(ans[15])
