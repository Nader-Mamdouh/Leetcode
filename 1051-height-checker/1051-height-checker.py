class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ex=sorted(heights)
        ans=0
        for i in range(len(heights)):
            if heights[i]!=ex[i]:
                ans+=1

        return ans