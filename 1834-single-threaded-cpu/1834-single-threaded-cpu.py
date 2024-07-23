import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        cpu = []
        ans = []
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t: t[0])
        
        i = 0
        time = tasks[0][0]
        while cpu or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(cpu, [tasks[i][1], tasks[i][2]])
                i += 1
            if not cpu:
                time = tasks[i][0]
            else:
                proc_time, idx = heapq.heappop(cpu)
                time += proc_time
                ans.append(idx)
        return ans
