class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        #firstList = [[0,2],[5,10],[13,23],[24,25]]
        #secondList = [[1,5],[8,12],[15,24],[25,26]]

        left = 0
        right = 0
        n = len(firstList)
        m = len(secondList)
        ans = []

        while left < n and right < m:
            if firstList[left][0] <= secondList[right][1] and secondList[right][0] <= firstList[left][1]:
                x = max(firstList[left][0], secondList[right][0])
                y = min(firstList[left][1], secondList[right][1])
                ans.append([x, y])

            if firstList[left][1] < secondList[right][1]:
                left += 1
            else:
                right += 1

        return(ans)