print("Counting frequency of a word in a string")

wordstring = input("Enter the string : ")

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("Frequencies\n" + str(wordfreq) + "\n")

print("Pairs\n" + str(list(zip(wordlist, wordfreq))))