class Solution(object):
    def vowelStrings(self, s, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefix=[0]
        anss=[]
        for word in s:
            if word[0] in vowels and word[-1] in vowels:
                prefix.append(1)
            else:
                prefix.append(0)

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        for q in range(len(queries)):
            ans = prefix[queries[q][1] + 1] - prefix[queries[q][0]]
            anss.append(ans)
        return(anss)
        