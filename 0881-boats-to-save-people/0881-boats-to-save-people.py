class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        start = 0
        end = len(people) - 1
        res = 0

        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            end -= 1
            res += 1

        return res
        