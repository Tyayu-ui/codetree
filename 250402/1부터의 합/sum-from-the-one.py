num = int(input())

sum = 0
for i in range(1, 101):
    if sum >= num:
        print(f"{i-1}")
        break
    sum+=i
