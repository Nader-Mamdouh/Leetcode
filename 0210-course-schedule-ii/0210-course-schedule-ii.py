class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        graph=defaultdict(list)
        indegree=defaultdict(int)
        q=deque([])
        ans=[]
        for post,pre in prerequisites:
            graph[pre].append(post)
            indegree[post]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i) 
        while q:
            course=q.popleft()
            ans.append(course)
            for j in graph[course]:
                indegree[j]-=1
                if indegree[j]==0:
                    q.append(j)
        if len(ans)<numCourses:
            return []
        else:
            return ans            