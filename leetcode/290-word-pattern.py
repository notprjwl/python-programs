def wordPattern(pattern, s):
    s = s.split(" ")

    if len(pattern) != len(s):
        return False
    
    hashmap = {}

    i = 0
    while i < len(pattern):
        if pattern[i] not in hashmap.keys() and s[i] not in hashmap.values():
            hashmap[pattern[i]] = s[i]
        i += 1
        print(hashmap)
    
    s = ''.join(s)
    value = ""
    for i in pattern:
        if i in hashmap.keys():
            value += hashmap.get(i)
        else:
            return False
    print(value, s)
    
    if value == s:
        return True
    return False
        
print(wordPattern(pattern = "jquery", s = "jquery"))