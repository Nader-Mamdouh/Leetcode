class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        from collections import defaultdict
        dic=defaultdict(int)
        for i in edges:
            dic[i[0]]+=1
            dic[i[1]]+=1
        maxx=max(dic, key=dic.get) 
        return maxx   