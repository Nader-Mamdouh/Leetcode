class Solution:
    def minOperations(self, logs):
        st = []
        for log in logs:
            if log == "../":
                if st:
                    st.pop()
            elif log != "./":
                st.append(log)
                
        return len(st)
