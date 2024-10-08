class Solution:
    def minSwaps(self, s: str) -> int:
        st=[]
        for i in range(len(s)):
            if st:
                if st[-1]=='[' and s[i]==']':
                    st.pop()
                else:
                    st.append(s[i])
            else:
                st.append(s[i])  
        if len(st)==0:
            return 0
        left=0
        right=len(st)-1
        swaps=0
        while left<right:
            if st[left]==']'and st[-1]=='[':
                swaps+=1
                left+=2
                right-=2
        return swaps        
                
