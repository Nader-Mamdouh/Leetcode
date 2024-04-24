

class Solution:
    def nextGreaterElement(self, num1, num2):
        ans = []
        next_greater = {}
        
        for i in range(len(num2)):
            greater = -1
            for j in range(i + 1, len(num2)):
                if num2[j] > num2[i]:
                    greater = num2[j]
                    break
            next_greater[num2[i]] = greater
        
        for num in num1:
            ans.append(next_greater.get(num, -1))
        
        return ans
