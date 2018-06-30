x = input("Write a phrase: ")
wordCount= {}
word_histogram = x.split(' ')

for word in word_histogram:
    wordCount[word] = x.count(word)
print(wordCount)
    