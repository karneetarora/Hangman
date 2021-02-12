file = open('wordlist.txt', 'r')
words = []
for item in file:
    if item not in words:
        words.append(item)
