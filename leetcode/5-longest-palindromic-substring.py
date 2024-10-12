# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

def substring(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            palin = s[i : j]
            print(palin)
            if palin == palin[::-1]:
                if len(palin) > len(longest):
                    longest = palin  #b bab 
    
    return longest

print(substring("babad"))