n = int(input())

def gkatn(n):
    num = 1
    for _ in range(n):
        for _ in range(n):
            if num == 10:
                num = 1
            print(num, end = " ")
            num+=1
        print()

gkatn(n)