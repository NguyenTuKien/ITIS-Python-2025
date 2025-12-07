def cal(n):
    res = 1
    while n != 0 : 
        res *= n % 10
        n //= 10
    return res

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(key=lambda x : (cal(x), x))
    for x in arr : 
        print(x, end=' ')
    print()