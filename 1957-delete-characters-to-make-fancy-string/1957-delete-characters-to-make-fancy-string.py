class Solution:
    def makeFancyString(self, s: str) -> str:
        st = []
        sim = 0 
        for i in s:
            if st:
                if st[-1] == i and sim == 2:
                    continue
                else:
                    if st[-1] == i:
                        sim += 1
                    else:
                        sim = 1
                    st.append(i)
            else:
                st.append(i)
                sim = 1  
                
        return ''.join(st)
