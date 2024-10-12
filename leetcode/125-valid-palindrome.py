
def isPalindrome(s):
    s = s.lower()
    result = ""
    for i in s:
        if i.isalnum():
            result += i
            
    if result == result[::-1]:
        return True
    else:
        return False

    
print(isPalindrome(s="A man, a plan, a canal: Panama"))
print(isPalindrome(s="0P"))
