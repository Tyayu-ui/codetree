A, B = map(int, input().split())
num = B - A + 1
for i in range(num):
    print(f"{B-i}", end = " ")