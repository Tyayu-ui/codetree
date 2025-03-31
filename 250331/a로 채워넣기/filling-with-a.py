word = input()

word1=word.replace(word[1], 'a',1)
word2=word1.replace(word[-2],'a',2)
print(word2)