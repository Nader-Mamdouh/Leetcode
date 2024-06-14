class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(index, prev1, prev2, count):
            if index == len(num):
                return count >= 3 
            for i in range(index + 1, len(num) + 1):
                if num[index] == '0' and i > index + 1:
                    break  
                
                curr = int(num[index:i])
                
                if count < 2 or curr == prev1 + prev2:
                    if backtrack(i, prev2, curr, count + 1):
                        return True
            
            return False
        return backtrack(0, 0, 0, 0)