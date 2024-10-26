class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        adj={ i : [] for i in range (n)}
       
        for i in range(n):
            x1,y1=points[i]
            for j in range(n):
                x2,y2=points[j]
                dis=abs(x1-x2)+abs(y1-y2)
                adj[i].append([dis,j])
                adj[j].append([dis,i])
        res=0
        st=set()
        minheap=[[0,0]]
        while len(st)!=n:
            cost,i=heapq.heappop(minheap)
            if i in st:
                continue
            res+=cost
            st.add(i)   
            for cost,neigh in adj[i]:
                if neigh not in st:
                    heapq.heappush(minheap,[cost,neigh])
        return res             

