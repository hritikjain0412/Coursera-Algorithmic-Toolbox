n = int(input())
arr = []
arr.append(0)
arr.append(1)
if n ==0:
    print(arr[0])

elif n==1:
    print(arr[1])

else:
    for i in range(2,n+1):
        x = arr[i-1] + arr[i-2]
        arr.append(x)


    print(arr[n])
    print(arr)
