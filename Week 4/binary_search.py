num = list(map(int,input().split()))
lis = list(map(int,input().split()))
num.pop(0)
lis.pop(0)
res = []
#print(num,lis)

low = 0
high = len(num)-1

def binary_search(num,low,high,key):
    while(low<=high):
        mid = (low + high) // 2

        if key == num[mid]:
            return mid
        elif key < num[mid]:
            high = mid - 1
        else:
            low = low + 1
    return -1
low = 0
high = len(num)-1
i = 0
#for i in range(len(lis)):
while(i<len(lis)):
    key=lis[i]
    x = binary_search(num,low,high,key)
    res.append(x)
    i += 1
fin = list(map(str,res))
print(" ".join(fin))
#for i in res:
#    print(i,end = ' ')
'''
seq = [int(i) for i in input().split()]
search_seq = [int(i) for i in input().split()]
n = seq[0]
seq = seq[1:]

def binary_search(seq, elt, r):
    l = 0
    while l<=r:
        m = (l+r)//2
        if elt > seq[m]:
            l = m + 1
        elif elt < seq[m]:
            r = m - 1
        else:
            return m
    return -1

soln = list()
for i in search_seq[1:]:
    ans = binary_search(seq, i, n-1)
    soln.append(ans)
print(' '.join([str(i) for i in soln]))
'''
