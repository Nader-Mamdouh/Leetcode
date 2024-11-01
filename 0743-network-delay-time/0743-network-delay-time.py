import heapq,sys
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for t in times:
            adj[t[0]].append((t[2],t[1]))
        q=[]
        heapq.heapify(q)
        dist = [sys.maxsize]*(n)
        dist[k-1]=0
        heapq.heappush(q,(0,k))
        while q:
            d,u = heapq.heappop(q)
            for weight,v in adj[u]:
                if dist[v-1]>dist[u-1]+weight:
                    dist[v-1]=dist[u-1]+weight
                    heapq.heappush(q,(dist[v-1],v))
        for i in range(len(dist)):
            if dist[i]==sys.maxsize:
                return -1
        return max(dist)