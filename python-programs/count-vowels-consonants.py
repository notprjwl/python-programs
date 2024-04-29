# Python program to count the Occurrence Of Vowels & Consonants in a String.

def count_vowels_consonants(text):
    vowels = list('aeiou')
    consonants = list('bcdfghijklmnpqrtvwxyz')
    number_of_vowels = 0
    number_of_consonants = 0
    for letter in text:
        if letter in vowels:
            number_of_vowels += 1
        elif letter in consonants:
            number_of_consonants += 1
            
    return f"number of vowels are: {number_of_vowels} and number of consolants are: {number_of_consonants}"
    
    
print(count_vowels_consonants('prajwal'))