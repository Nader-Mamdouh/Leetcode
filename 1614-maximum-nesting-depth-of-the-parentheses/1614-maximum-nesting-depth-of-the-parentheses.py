class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxxDepth = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
                maxxDepth = max(maxxDepth, len(stack))
            elif ch == ')':
                stack.pop()
        return maxxDepth
        