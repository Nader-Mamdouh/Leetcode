class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        max_endpoint = max(interval[1] for interval in intervals)   
        pre = [0] * (max_endpoint + 2)
        for left, right in intervals:
            pre[left] += 1
            pre[right + 1] -= 1
        
        max_groups = 0
        current_groups = 0
        for i in range(max_endpoint + 1):
            current_groups += pre[i]
            max_groups = max(max_groups, current_groups)
        
        return max_groups
