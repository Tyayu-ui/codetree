start, end = map(int, input().split())
num = 0
total = 0

for i in range(start, end + 1):
    for j in range(1, i+1):
        if i%j == 0:
            num +=1
    if num == 3:
        total+=1
    num = 0
print(total)
