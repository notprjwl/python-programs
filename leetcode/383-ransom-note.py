
def canConstruct(ransomNote, magazine):
    if ransomNote and magazine == "":
        return True
    
    result = ""
    
    for i in range(len(ransomNote)):
        found = False
        for j in range(len(magazine)):
            if ransomNote[i] == magazine[j]:
                magazine = magazine[:j] + magazine[j+1:]    # if it is a match then remove the letter
                result += ransomNote[i] # optional - add that letter to result to check if it is equal
                found = True
                break
    
    if not found:
        return False
    
    if result == ransomNote:            
        return True
    return False
    

print(canConstruct(ransomNote = "fffbfg", magazine = "effjfggbffjdgbjjhhdegh"))