num = list(map(int, input().split()))
print(f"{num[0]} {num[1]}", end = " ")

for i in range(8):
    if num[0]+num[1] >= 10:
        num[0], num[1] = num[1], num[0]+num[1]-10
        print(f"{num[1]}", end=" ")
    else:
        num[0], num[1] = num[1], num[0]+num[1]
        print(f"{num[1]}", end=" ")

        