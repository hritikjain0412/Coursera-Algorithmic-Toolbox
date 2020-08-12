def gcd(a,b):
    if b == 0:
        print(a)

    else:
        c = a % b

        return gcd(b,c)
a,b = map(int,input().split())
gcd(a,b)
