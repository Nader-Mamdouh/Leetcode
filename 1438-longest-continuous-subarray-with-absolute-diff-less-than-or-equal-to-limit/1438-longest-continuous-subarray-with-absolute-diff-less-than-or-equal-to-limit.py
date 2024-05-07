class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx=deque()
        mn=deque()
        ans=0
        l=0
        r=0

        while l<=r and r<len(nums):

            while mn and mn[-1] > nums[r]:
                mn.pop()
            mn.append(nums[r])

            while mx and mx[-1] < nums[r]:
                mx.pop()
            mx.append(nums[r])

            while mx[0] - mn[0] > limit:
                if mx[0] == nums[l]:
                    mx.popleft()
                if mn[0] == nums[l]:
                    mn.popleft()
                l+=1

            r+=1

            ans=max(ans,r-l)
        
        return ans