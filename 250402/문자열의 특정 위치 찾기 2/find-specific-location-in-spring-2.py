fruits = ["apple","banana","grape","blueberry","orange"]
ch = input()
cnt = 0

for fruit in fruits:
    if fruit[2] == ch or fruit[3] == ch:
        print(f"{fruit}")
        cnt += 1
print(f"{cnt}")
