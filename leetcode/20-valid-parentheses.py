class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')' or i == '}' or i == ']':
                if not stack:
                    return False
                top_element = stack.pop()
                if (i == ')' and top_element != '(') or (i == '}' and top_element != '{') or (i == ']' and top_element != '['):
                    return False
        return not stack

solution = Solution()
print(solution.isValid("()[][][][]"))

# class Solution(object):
#     def isValid(self, s):
#         stack = []
#         for i in s:
#             if i == '(' or i == '{' or i == '[':
#                 stack.append(i)
#             elif i == ')' or i == '}' or i == ']':
#                 if not stack:
#                     return False
#                 top_element = stack.pop()
#                 if (i == ')' and top_element != '(') or \
#                    (i == '}' and top_element != '{') or \
#                    (i == ']' and top_element != '['):
#                     return False
        
#         return not stack

# # Create an instance of the Solution class
# solution = Solution()
# print(solution.isValid("()[][][][]"))  # Output: False