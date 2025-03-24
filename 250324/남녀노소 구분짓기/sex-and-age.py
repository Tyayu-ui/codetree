gender = int(input())
year = int(input())

if gender == 0:
    if year >= 19:
        print("MAN")
    else:
        print("BOY")
else:
    if year >= 19:
        print("WOMAN")
    else:
        print("GIRL")