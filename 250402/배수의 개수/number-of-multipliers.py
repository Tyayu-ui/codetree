multiple_of_3 = 0
multiple_of_5 = 0

for i in range(10):
    num = int(input())
    if num % 3==0:
        multiple_of_3 += 1
    if num % 5==0:
        multiple_of_5 += 1
print(f"{multiple_of_3} {multiple_of_5}")
    
