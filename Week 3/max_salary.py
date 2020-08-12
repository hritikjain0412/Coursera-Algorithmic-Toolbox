def isgreater(i,high_no):
    i = str(i)
    hi = str(high_no)
    a = i + hi
    b = hi + i
    if int(a)>int(b):
        return True
    else:
        return False

def max_salary(sal):
    max_sal = []
    while sum(sal)!=0:
        high_no = 0
        for i in sal:
                if isgreater(i,high_no):
                    high_no = i

        max_sal.append(high_no)
        sal.remove(high_no)
    max_sal = list(map(str,max_sal))
    return max_sal

n = int(input())
sal = list(map(int,input().split()))

#print("sal",sal)
ans = max_salary(sal)
print(''.join(ans))
