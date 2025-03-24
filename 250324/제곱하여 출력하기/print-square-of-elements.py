num = int(input())
list1 = list(map(int, input().split()))
for i in range(num):
    print(f"{list1[i]*list1[i]}", end = " ")