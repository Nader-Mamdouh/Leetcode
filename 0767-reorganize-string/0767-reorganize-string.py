import heapq
from collections import defaultdict

class Solution:
    def reorganizeString(self, s: str) -> str:
        s2 = ""
        dic = defaultdict(int)
        
        # Count the frequency of each character
        for char in s:
            dic[char] += 1
        
        heap = []
        
        # Create a max heap based on the frequency of characters (use negative frequency)
        for ch, freq in dic.items():
            heapq.heappush(heap, (-freq, ch))
        
        for _ in range(len(s)):
            if not heap:
                break
            
            mx_freq, ch1 = heapq.heappop(heap)
            
            if s2 == "" or s2[-1] != ch1:
                s2 += ch1
                if -mx_freq > 1:
                    heapq.heappush(heap, (mx_freq + 1, ch1))  # Increment toward 0
            else:
                if not heap:
                    return ""
                
                mx_freq2, ch2 = heapq.heappop(heap)
                s2 += ch2
                if -mx_freq2 > 1:
                    heapq.heappush(heap, (mx_freq2 + 1, ch2))  # Increment toward 0
                heapq.heappush(heap, (mx_freq, ch1))
        
        return s2
