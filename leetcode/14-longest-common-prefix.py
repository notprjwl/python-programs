strs = ["flower","flow","flight"]

def longest_common_prefix(strs):
    result = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i==len(s) or s[i] != strs[0][i]:
                return result
        result += strs[0][i]
            
                
        
            
    

print(longest_common_prefix(strs))