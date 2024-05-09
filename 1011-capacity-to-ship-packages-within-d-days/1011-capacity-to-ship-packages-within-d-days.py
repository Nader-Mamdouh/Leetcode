class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            n = 1
            total_weight = 0
            
            for weight in weights:
                if total_weight + weight > mid:
                    n += 1
                    total_weight = 0
                total_weight += weight
            
            if n <= days:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
