A, B, C = map(int, input().split())
if A > B > C or C > B > A:
    print(f"{B}")
elif B > C > A or A > C > B:
    print(f"{C}")
elif B > A > C or C > A > B:
    print(f"{A}")