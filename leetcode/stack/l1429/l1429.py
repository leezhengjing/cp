class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        counter = 0
        for i in range(len(s)):
            if s[i] == '(':
                counter += 1
            if s[i] == ')':
                if counter == 0:
                    continue
                counter -= 1
            stack.append(s[i])
        final = []
        counter = 0
        for char in reversed(stack):
            if char == '(':
                if counter == 0:
                    continue
                counter -= 1
            if char == ')':
                counter += 1
            final.append(char)
        return ''.join(reversed(final))
    
# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
#         stack = []
#         final = []
#         for i in range(len(s)):
#             if s[i] == '(':
#                 stack.append(len(final))
#             if s[i] == ')':
#                 if stack:
#                     stack.pop()
#                 else:
#                     continue
#             final.append(s[i])
#         for j in stack:
#             final[j] = ''
#         return ''.join(final)