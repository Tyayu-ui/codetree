num = int(input())
arr = [i+1 for i in range(num)]
for i in range(num):
    for j in range(num):
        if j%2!=0:
            print(arr[-i-1], end="")
        else:
            print(arr[i], end="")
    print()