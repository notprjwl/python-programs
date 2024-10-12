def intToRoman(num):
    hashmap = {
           1:    'I',
           4:    'IV',
           5:    'V',
           9:    'IX',
          10:    'X',
          40:    'XL',
          50:    'L',
          90:    'XC',
         100:    'C',
         400:    'CD',
         500:    'D',
         900:    'CM',
        1000:    'M'
    }

    num = str(num)
    numsArray = []
    for i in range(len(num)):
        splittedNum = (int(num[i]) * (10 ** (len(num) - i - 1)))
        numsArray.append(splittedNum)
    
    result = ""
    for n in numsArray:
        if n > 0:
            for value in sorted(hashmap.keys(), reverse=True):
                while n >= value:
                    result += hashmap[value]
                    n -= value
    
    return result

print(intToRoman(3749))