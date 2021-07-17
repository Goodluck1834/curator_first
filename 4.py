f = open('4a.txt')
n = int(f.readline())

k  = 8
buf = [0] * k
znach = 0
ans = 0

for i in range(k):
    x = int(f.readline())
    buf[i] = x

for i in range(k, n):
    if buf[0] % 2 == 1 and buf[0] > znach:
        znach = buf[0]        
    x = int(f.readline())
    if x % 2 == 1:
        if x * znach > ans:
            ans = x * znach       
    for j in range(k-1):
        buf[j] = buf[j+1]
    buf[k-1] = x
    
print(ans)    
