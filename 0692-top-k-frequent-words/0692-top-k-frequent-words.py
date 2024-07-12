from typing import List
import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = defaultdict(int)
        for word in words:
            dic[word] += 1
        heap = []
        ans = []
        for word, count in dic.items():
            heapq.heappush(heap, (-count, word))
        for _ in range(k):
            freq, word = heapq.heappop(heap)
            ans.append(word)
        
        return ans