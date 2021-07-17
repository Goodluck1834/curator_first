f = open('2b.txt')
n = int(f.readline())

summ = 0
first = 10**10
last = 0

for i in range(n - 1):
    x = int(f.readline())
    summ += x
    first = min(first, x)
    last = max(last, x)
need = (first + last) / 2 * n
missed = need - summ
ans = missed - first +1

f.close

print(int(ans))
