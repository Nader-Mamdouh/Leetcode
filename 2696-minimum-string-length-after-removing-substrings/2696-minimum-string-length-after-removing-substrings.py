class Solution:
    def minLength(self, s: str) -> int:
        from collections import defaultdict
        dic=defaultdict(int)
        st=[]
        for i in range(len(s)):
            if st:
                if st[-1] =='A' and s[i]=='B':
                    st.pop()
                elif st[-1] =='C' and s[i]=='D':
                    st.pop() 
                else:
                    st.append(s[i])    
            else:
                st.append(s[i])       

        return len(st)               

