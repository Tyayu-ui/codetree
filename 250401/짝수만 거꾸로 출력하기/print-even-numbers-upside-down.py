num = int(input())
num_list = map(int, input().split())

odd_list = []
for i in num_list:
    if i%2==0:
        odd_list.append(i)

for i in range(len(odd_list)-1, -1, -1):
    print(odd_list[i], end = " ")
