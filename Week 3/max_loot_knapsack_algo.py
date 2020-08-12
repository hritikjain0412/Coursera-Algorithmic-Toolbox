def knapsack(W,weigh,val):
    v = 0
    for i in range(n):
        if W == 0:
            return v
        else:
            a = min(dic[vperw[i]],W)
            v = v + (a*vperw[i])
            W = W - a
    return v

n,W = list(map(int,input().split()))
val = []
weigh = []
vperw = []
#finaldict = {}
for i in range(n):
    x,y = list(map(int,input().split()))
    vpw = x/y
    val.append(x)
    weigh.append(y)
    vperw.append(vpw)
dic = dict(zip(vperw,weigh))
vperw.sort(reverse = True)

print('%.4f'%knapsack(W,weigh,val))


'''
for i in sorted(dic):
    finaldict.update({i:dic[i]})
print("sorted",finaldict)

print("dict",dic[6])
print(val)
print(weigh)
print(vperw)
'''
