A, B = map(int, input().split())

while A <= B:
    if A % 2 == 0:
        print(f"{A}", end=" ")
        A += 3
    else:
        print(f"{A}", end=" ")
        A *= 2
        
        