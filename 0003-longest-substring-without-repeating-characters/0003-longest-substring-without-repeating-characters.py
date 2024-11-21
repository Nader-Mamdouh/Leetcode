class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        dic=defaultdict(int)
        ans=0
        for right in range(len(s)):
            dic[s[right]]+=1

            while dic[s[right]]>1:
                dic[s[left]]-=1
                if dic[s[left]]==0:
                    del dic[s[left]]
                left+=1
            ans=max(ans,right-left+1)   
        return ans         
