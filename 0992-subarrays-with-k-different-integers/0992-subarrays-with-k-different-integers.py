class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=j1=j2=cnt_unique1=cnt_unique2=0
        cnt1,cnt2=[0]*(n+1),[0]*(n+1)
        for i in range(n):
            while j1<n and cnt_unique1<k:
                cnt_unique1+=(cnt1[nums[j1]]==0)
                cnt1[nums[j1]]+=1
                j1+=1
            
            while j2<n and cnt_unique2<=k:
                cnt_unique2+=(cnt2[nums[j2]]==0)
                cnt2[nums[j2]]+=1
                j2+=1
                
           
            if cnt_unique1+1==cnt_unique2 and cnt_unique1==k:
                ans+=j2-j1
            elif cnt_unique1==cnt_unique2 and cnt_unique1==k:
                ans+=j2-j1+1
                
            cnt_unique1-=(cnt1[nums[i]]==1)
            cnt_unique2-=(cnt2[nums[i]]==1)
            cnt1[nums[i]]-=1
            cnt2[nums[i]]-=1

        return ans
                