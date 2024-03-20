from collections import defaultdict
class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        


        dic = defaultdict(int)

        for i in s:
            dic[i] += 1

        s2 = ""
        n = len(s)
        one = dic['1']
        print(one)
        for i in range(n - one + 1):
            if i == 0:
                s2 += '1'
                dic['1'] -= 1
            else:
                s2 += '0'

        for i in range(n - one + 1, n):
            s2 += '1'

        s3 = s2[::-1]
        return(s3)
        