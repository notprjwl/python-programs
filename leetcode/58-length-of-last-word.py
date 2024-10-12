def lengthOfLastWord(s):
    word = ""
    wordList = []
    for i in s:
        if i != " ":
            word += i
        else:
            if word:
                wordList.append(word)
                word = ""
    if word:
        wordList.append(word)
    return len(wordList[-1])
            
            


print(lengthOfLastWord("Hello World"))