# def strStr(haystack, needle):
#     if needle not in haystack:
#         return -1
    
#     string = ""
#     for i in range(len(haystack)):
#         for j in range(len(needle)):
#             if needle[j] == haystack[i]:
#                 string += haystack[i]
#                 if string == needle:
#                     print(i, haystack[i])
#                     return (i - (len(needle)-1))
                

# print(strStr(haystack = "hello", needle = "ll"))


def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    
    for i in range(len(haystack)):
        print(haystack[i : i + len(needle)])
        if haystack[i : i + len(needle)] == needle:
            return i
    
    return -1
    
    
print(strStr(haystack = "hello", needle = "ll"))
