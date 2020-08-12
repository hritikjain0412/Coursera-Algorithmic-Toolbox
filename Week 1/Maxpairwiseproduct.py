n = int(input())
#m = input().split(" ")
#num = list(map(int,m))
num = [int(x) for x in input().split(" ")]
num.sort(reverse = True)
result = num[0]*num[1]
print(result)
