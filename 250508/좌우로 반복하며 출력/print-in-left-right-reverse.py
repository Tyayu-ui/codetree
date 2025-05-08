num = int(input())
arr = [i+1 for i in range(num)]
for i in range(num):
    for j in range(num):
        if i%2!=0:            
            print(arr[-j-1],end="")
        else:
            print(arr[j], end="")
    print()