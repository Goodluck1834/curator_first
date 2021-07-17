f = open('5b.txt')
contr = int(f.readline())
n = int(f.readline())
summ = 0
now = []
ans = 10**10
flag = 0

for i in range(n):
    x = int(f.readline())
    now.append(x)
    summ += x
    if summ < contr and contr - summ < ans:
        flag = 0
        ans = contr - summ
    while summ > contr:
        if contr != summ and summ - contr < ans:
            flag = 1
            ans = summ - contr
        summ -= now[0]
        now.pop(0)
    if contr < summ and contr - summ < ans:
        flag = 0
        ans = contr - summ
    
if flag == 1:
    print(contr + ans)
else:
    print(contr - ans)
