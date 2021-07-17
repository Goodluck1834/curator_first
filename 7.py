f = open('7b.txt')
n = int(f.readline())
b = 0
mas = [b] * 13
rez = [b] * 13
need = 0

x, y = map(int, f.readline().split())
mas[max(x,y) % 13] = max(x,y)
mas[min(x,y) % 13] = min(x,y)


for i in range(n-1):
    x, y = map(int, f.readline().split())
    for j in range(13):
        if mas[j] != 0:
            if (mas[j] + x) > rez[(mas[j] + x) % 13]:
                rez[(mas[j] + x) % 13] = mas[j] + x
            if (mas[j] + y) > rez[(mas[j] + y) % 13]:
                rez[(mas[j] + y) % 13] = mas[j] + y
    for j in range(13):
        mas[j] = rez[j]
        rez[j] = b
        
mas[0] = 0
for i in range(13):
    if mas[i] != 0 and mas[i] > need:
        need = mas[i]
        
print(need)

f.close()

                
    
    
