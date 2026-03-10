from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap , (-count, num))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result