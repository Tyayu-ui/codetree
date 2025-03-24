N, M = map(int, input().split())
print(f"{N}")

while N // M != 0:
    print(f"{N//M}")
    N //= M
