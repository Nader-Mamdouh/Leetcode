class Solution(object):
    def vowelStrings(self, s, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        anss=[]
        prefix=[0]
        for i in range(len(s)):
            if s[i][0]=='a' or s[i][0]=='e' or s[i][0]=='i' or s[i][0]=='o' or s[i][0]=='u' and s[i][-1]=='a' or s[i][-1]=='e' or s[i][-1]=='i' or s[i][-1]=='o' or s[i][-1]=='u':
                prefix.append(1)
            else:
                prefix.append(0)
        for i in range (1,len(prefix)) :
            prefix[i]+=prefix[i-1]
        #print(prefix)
        for q in range(len(queries)):
            ans=prefix[queries[q][1]+1]-prefix[queries[q][0]]
            anss.append(ans)
        return anss    
           
        