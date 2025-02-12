class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for val in nums:
            freq[val] += 1

        pq = []

        for entry in freq:
            heapq.heappush(pq, (-freq[entry], entry))
        
        ans = []
        while k > 0:
            ans.append(heapq.heappop(pq)[1])
            k -= 1

        return ans