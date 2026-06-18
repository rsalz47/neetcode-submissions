from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []

        return list(map(lambda e: e[0], Counter(nums).most_common(k)))

        
