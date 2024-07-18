class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import defaultdict
        dic=defaultdict(int)
        for i in arr:
            dic[i]+=1
        st=set()
        for key , value in dic.items():
            st.add(value)  
        return len(dic)==len(st)      