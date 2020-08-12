n = int(input())
num = list(map(int,input().split()))
num.sort()
for i in range(n):
    print(num[i],end = ' ')
