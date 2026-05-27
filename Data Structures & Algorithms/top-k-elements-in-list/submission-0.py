class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = {}

        for num in nums:
            if num in buckets:
                buckets[num] += 1
            else:
                buckets[num] = 1

        result = []
        while k > 0:
            result.append(max(buckets, key=buckets.get))
            buckets[result[-1]] = 0
            k -= 1

        return result