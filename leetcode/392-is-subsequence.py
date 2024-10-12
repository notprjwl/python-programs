
# def isSubsequence(s, t):
#     result = ""
#     for i in t:
#         if i in s:
#             result += i
#     print(result)
#     print(s)
#     if result == s:
#         return True
#     return False

# print(isSubsequence(s = "ab", t = "baab"))


def isSubsequence(s, t):
    count = 0
    res = ""
    index = 0
    for i in range(len(s)):
        for j in range(index, len(t)):
            if s[i] == t[j]:
                count += 1
                res += s[i]
                index = j + 1
                break 
    return count == len(s) and res == s
                

print(isSubsequence(s = "acb", t = "ahbgdc"))
