row, col = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(row)]
arr2 = [list(map(int, input().split())) for _ in range(row)]
arr3 = [[0 for _ in range(col)] for _ in range(row)]

for i in range(row):
    for j in range(col):
        if arr1[i][j] == arr2[i][j]:
            arr3[i][j] = 0
        else:
            arr3[i][j] = 1

for i in range(row):
    for j in range(col):
        print(arr3[i][j], end=" ")
    print()