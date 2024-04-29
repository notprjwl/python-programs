# Counting the Number of Occurances of a Character in a String

def occurances(word, char):
    count = 0
    for i in word:
        if i in char:
            count += 1

    return count


word = "prajwal"
character = "a"
print(occurances(word, character))