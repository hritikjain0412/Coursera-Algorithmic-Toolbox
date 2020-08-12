def max_no_of_prizes(n):
    if n <= 2:
        print("1")
        print(n)
    else:
        arr = []
        for i in range(1,n):
            arr.append(i)
            if sum(arr)<n:
                continue
            else:
                break
        last = n - sum(arr)
        if last == 0:
            print(len(arr))
            arr = list(map(str,arr))
            print(" ".join(arr))
        else:
            for i in range(n):
                if last>len(arr):
                    arr.append(last)
                    print(len(arr))
                    arr = list(map(str,arr))
                    print(" ".join(arr))
                    break
                else:
                    arr.pop()
                last = n - sum(arr)
n = int(input())
max_no_of_prizes(n)
