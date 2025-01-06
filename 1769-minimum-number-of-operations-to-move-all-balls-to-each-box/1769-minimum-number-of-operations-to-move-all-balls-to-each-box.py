class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        sum = 0

        ans2 = []

        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    sum += abs(j - i)
            ans2.append(sum)
            sum = 0


        return(ans2)