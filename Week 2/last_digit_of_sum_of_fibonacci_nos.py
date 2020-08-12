'''
def fibonacci(n):
    arr = [0,1]
    if n <= 1:
        return n

    else:
        for i in range(2,n+1):
            x = arr[i-1] + arr[i-2]
            arr.append(x)

    return(arr)


n = int(input())

f = str(sum(fibonacci(n)))

print(f[-1])
'''

def fib(n):
    f0 = 0
    f1 = 1
    if n <= 1:
        return n

    rem = n % 60

    if rem == 0:
        return 0

    else:
        for i in range(2,rem+3):
            f = (f0 + f1) % 60
            f0 = f1
            f1 = f
        s = f1 - 1
        return s

n = int(input())
result = fib(n)%10
print(result)
