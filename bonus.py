from operator import itemgetter
word = input("write a word: ")
letters = {}

for i in word:
    letters[i] = word.count(i)

topLetters = sorted(letters, key=letters.__getitem__, reverse=True)
print(topLetters[0:3])