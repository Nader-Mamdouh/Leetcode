class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        tr=times[targetFriend][0]
        times.sort()
        
        ans=0
        for i in range(len(times)):
            if times[i][0]<tr and times[i][1]>tr:
                ans+=1
        return ans        

