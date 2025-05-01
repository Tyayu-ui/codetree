num = int(input())

for _ in range(num):
    a, b = map(int,input().split())
    sum = 0
    for i in range(a, b+1):
        if i%2==0:
            sum+=i
    print(sum)
    sum = 0