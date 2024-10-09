class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        for i in s:
            if st:
                if st[-1]=='(' and i==')':
                    st.pop()
                else:
                    st.append(i)
            else:
                st.append(i)
        return len(st)                    