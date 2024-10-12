def isIsomorphic(s, t):
    hashmap = {}
    
    i = 0
    while i< len(s):
        if s[i] not in hashmap.keys() and t[i] not in hashmap.values():
            hashmap[s[i]] = t[i]
        else:
            i += 1   
    print(hashmap)
    
    value = ""
    for i in s:
        if i in hashmap.keys():
            value += hashmap.get(i)
        else:
            return False
    
    if value == t:
        return True
    return False
       

print(isIsomorphic("badc", "baba"))