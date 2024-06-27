class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graphRed=defaultdict(list)
        graphBlue=defaultdict(list)

        for u,v in redEdges:
            graphRed[u].append(v)

        for u,v in blueEdges:
            graphBlue[u].append(v)

        vis=defaultdict(bool)
        q=deque([(0,'r'),(0,'b')])
        vis[(0,'r')]=True
        vis[(0,'b')]=True
        ans=[-1 for _ in range(n)]
        dist=0

        while q:
            for i in range(len(q)):
                node,color=q.popleft()

                if ans[node]==-1:
                    ans[node]=dist

                if color == 'r':
                    for child in graphBlue[node]:
                        if not vis[(child,'b')]:
                            q.append((child,'b'))
                            vis[(child,'b')]=True
                else:
                    for child in graphRed[node]:
                        if not vis[(child,'r')]:
                            q.append((child,'r'))
                            vis[(child,'r')]=True
            dist+=1

        return ans


        

