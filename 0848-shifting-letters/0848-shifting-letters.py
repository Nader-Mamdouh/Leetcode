class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        ss = []
        ans = ""

        cumulative_sum = 0


        for i in range(len(shifts) - 1, -1, -1):
            cumulative_sum += shifts[i]
            shifts[i] = cumulative_sum
        #print(shifts)
        for char in s:
            ss.append(ord(char) - ord('a'))


        for i in range(len(shifts)):
            ss[i] = (ss[i] + shifts[i]) % 26

        for i in ss:
            ans += chr(i + ord('a'))

        return(ans)
        