class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        s=sorted(seats)
        t=sorted(students)
        ans=0
        n=len(s)
        for i in range(n):
            ans+=abs(t[i]-s[i])
        return ans    