class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for val in nums:
            freq[val] += 1

        pq = []

        for val, amount in freq.items():
            heappush(pq, (-amount, val))
        
        ans = []

        while k > 0:
            ans.append(pq[0][1])
            heappop(pq)
            k -= 1
        
        return ans