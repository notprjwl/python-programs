strs = ["dog","racecar","car"]

# def longest_common_prefix(strs):
#     result = ""
#     for i in range(len(strs[0])):
#         for s in strs:
#             if i==len(s) or s[i] != strs[0][i]:
#                 return result
#         result += strs[0][i]
            
                
# print(longest_common_prefix(strs))


def longest_common_prefix(strs):
    prefix = strs[0]
    for i in range(len(prefix)):
        for j in range(len(strs)):
            if i >= len(strs[j]) or strs[j][i] != prefix[i]: 
                return prefix[:i]     
    return prefix
        
        
print(longest_common_prefix(strs))



