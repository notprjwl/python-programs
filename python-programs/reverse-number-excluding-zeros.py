# 230 -> 32

def reversedNumber(numInt):
    num = str(numInt)
    if num[-1] == "0":
        result = num[0:len(num)-1]
    return result[::-1]
    
print(reversedNumber(230))