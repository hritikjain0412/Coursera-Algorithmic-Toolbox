def pisano(n):
    pre = 0
    current = 1
    for i in range(n*n):
        pre,current = current,(pre+current)%n

        if pre==0 and current == 1:
            return i+1

def fibnonacci(x):
    arr = [0,1]

    if x == 0:
        return 0

    elif x == 1:
        return 1

    else:

        for i in range(2,x+1):
            y = arr[i-1] + arr[i-2]
            arr.append(y)
        return arr[x]
#print(pisano(1000))
#print(pisano(10))
m,n = map(int,input().split())

x = m % pisano(n)

result = fibnonacci(x) % n
print(result)
