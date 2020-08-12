def fib(n):
    f0 = 0
    f1 = 1
    if n<= 0:
        return 0
    if n == 1:
        return 1
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

m,n = map(int,input().split())

res = fib(n) - fib(m-1)
print(res % 10)
