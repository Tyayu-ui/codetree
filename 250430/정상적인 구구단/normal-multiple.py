num = int(input())
for i in range(1,num+1):
    for j in range(1,num+1):
        if num == j:
            print(f"{i} * {j} = {i*j}")
        else:
            print(f"{i} * {j} = {i*j}", end=(', '))
