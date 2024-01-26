def palindrome(text):
    
    if(text == text[::-1]):
        return "it is a palindrome"
    else:
        return "not a palindrome"




text = input("enter a text: ")
print(palindrome(text))