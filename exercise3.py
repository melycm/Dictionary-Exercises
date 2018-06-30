word = input("write a word: ")
letters = {}

for i in word:
    letters[i] = word.count(i)
print(letters)
