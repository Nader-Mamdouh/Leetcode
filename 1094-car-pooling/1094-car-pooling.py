class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        ans=[0]*10000
        for pas,fromm,too in trips:
            ans[fromm]+=pas
            ans[too]-=pas
        for i in range(1,len(ans)):
            ans[i]+=ans[i-1]
            if ans[i]>capacity:
                return False
        return True        

        