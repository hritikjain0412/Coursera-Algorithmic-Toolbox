
n = int(input())
arr = [0,1]

if n == 0:
    print(arr[0])

elif n == 1:
    print(arr[1])



else:
    for i in range(2,n+1):
        x = (arr[i-1] + arr[i-2])%10
        arr.append(x)

    #f = arr[n] % 10

    print(arr[n])
