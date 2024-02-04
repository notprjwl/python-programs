# Python program to delete vowels in a given string.

def delete_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for letter in vowels:
        if letter in text:
            text = text.replace(letter, "")
    return text

print(delete_vowels('prajwal'))