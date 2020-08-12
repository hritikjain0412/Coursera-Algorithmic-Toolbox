def car_fueling(d,m,num):

    currentrefill = 0
    lastrefill = 0
    refills = 0
    #for currentrefill in range(len(num)-1):
    while(currentrefill<(len(num)-1)):
    #while num[lastrefill]+m<d:
        lastrefill = currentrefill

        while(currentrefill<len(num)-1) and num[currentrefill+1]-num[lastrefill]<=m :
            currentrefill = currentrefill + 1
        if currentrefill == lastrefill:
            return "-1"
        if currentrefill < (len(num) - 1):
            refills += 1
            '''
        if num[lastrefill]+m < d:
            refills = refills + 1
            '''
    return refills

d = int(input())
m = int(input())
n = int(input())
num = list(map(int,input().split()))
num.insert(0,0)
num.insert(len(num),d)
#print(num)
print(car_fueling(d,m,num))
