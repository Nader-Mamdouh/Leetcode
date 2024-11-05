class Solution:
    def minChanges(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(0,n-1,2):
            st=set()
            st.add(s[i])
            st.add(s[i+1])
            if len(st)==2:
                ans+=1
        return ans        