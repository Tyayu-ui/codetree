word = input().split()

if len(word[0]) > len(word[1]):
    print(word[0], end=" ")
    print(len(word[0]))
elif len(word[0]) < len(word[1]):
    print(word[1], end=" ")
    print(len(word[1]))
else:
    print("same")
