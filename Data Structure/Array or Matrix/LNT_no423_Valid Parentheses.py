class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):

        stack = []
        if len(s) == 0 or len(s) % 2 != 0:
            return False

        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)

            elif not stack:
                return False

            elif ch == ']' and stack[-1] == '[' or ch == ')' and stack[-1] == '(' or ch == '}' and stack[-1] == '{':
                stack.pop()

        return not stack

if __name__=='__main__':
    ans = Solution()
    print(ans.isValidParentheses("([)]"))