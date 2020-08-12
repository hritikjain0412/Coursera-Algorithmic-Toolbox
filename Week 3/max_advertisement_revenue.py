n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort(reverse = True)
b.sort(reverse = True)
#print(a,b)
c = []
for i in range(n):
    r = a[i]*b[i]
    c.append(r)

print(sum(c))
