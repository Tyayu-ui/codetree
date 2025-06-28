n, m = map(int, input().split())

num = 1
result = 1
for i in range(1, max(n, m)):
    if n % num == 0 and m % num == 0:
        result = num
    num+=1
print(result)