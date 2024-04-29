# # list1 = [1, 2 ,3 ,4 ,5]
# # for i in list1:
# #     print(list1[i])

# for _ in range(5):
#     firstSelection = input('Enter your selection - a, b, c or d: ')
#     match firstSelection:
#         case "a":
#             print("print a")
              
#         case "b":
#             print("print b")
        
#         case "c": 
#             break

# Input
def findTheDifference(self, str1, str2):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
    for char in str1:
        if char not in str2:
            return char

    for char in str2:
        if char not in str1:
            return char


str1 = input()
str2 = input()

            