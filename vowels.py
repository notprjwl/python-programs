# Python program to check given character is vowel or consonant.

def check_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in word:
        if i in vowels:
            return True
    return False
    
word = 'pyth0n'
if check_vowel(word):
    print(f'{word} is a vowel')
else:
    print(f'{word} is not a vowel')