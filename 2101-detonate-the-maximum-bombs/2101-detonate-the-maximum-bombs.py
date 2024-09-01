class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        mx=0
        n=len(bombs)
        for i in range(n):
            visited=[0]*n
            temp=1
            queue=[(bombs[i])]
            visited[i]=1
            while queue:
                x=queue.pop(0)
                for j in range(n):
                    if visited[j]==0 and((x[0]-bombs[j][0])**2+(x[1]-bombs[j][1])**2)<=x[2]**2:
                        temp+=1
                        queue.append((bombs[j]))
                        visited[j]=1
            mx=max(mx,temp)
        return mx