class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        ans=[0]*(n+1)
        for first,last,seat in bookings:
            ans[first-1]+=seat
            ans[last]-=seat
        for i in range(1,n+1):
            ans[i] += ans[i-1]

        return ans[:-1]