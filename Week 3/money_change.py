def moneychange(x):
    count = 0
    if x>=10:
        res = x//10
        y = x %10
        count =count + res
        x = y
    if x<10 and x>=5:
        res = x // 5
        y = x%5
        count = count + res
        x = y
    if x<5 and x >=1:
        res = x//1
        count = count + res
    return count

x = int(input())
print(moneychange(x))
