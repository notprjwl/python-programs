class Solution:
    def romanToInt( s: str) -> int:
        roman_dic = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        result = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        for i in s:
            if i in roman_dic:
                result += roman_dic[i]
        print(result)
        
    romanToInt('MCMXCIV')