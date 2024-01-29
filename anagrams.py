# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#egL SILENT -> LISTEN


def anagram(str1, str2):
    count = 0
    for i in str1:
        for j in str2:
            if i == j:
                count += 1
                
    if count == len(str1):
        return 'Strings are anagram'
    else:
        return "Strings are not anagram"
    
str1 = "silent"
str2 = "listen"
print(anagram(str1, str2))