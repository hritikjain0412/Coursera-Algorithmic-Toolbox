'''
def lcm(a,b):
    if a > b:
        great = a

    else :
        great = b

    while(True):

        if((great%a == 0) and (great % b == 0)):
            print(great)
            break
        else:
            great +=1
a,b = map(int,input().split())
lcm(a,b)
'''
def gcd(a,b):
    if b == 0:
        return a

    else:
        c = a%b
        return gcd(b,c)

def lcm(a,b):
    x = a*b
    lcm = x //
     gcd(a,b) ##FORMULA : A*B = LCM(A,B) * GCD(A,B)

    return lcm
a,b = map(int,input().split())
print(lcm(a,b))
