class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            target_pair = target - nums[i]
            
            try:
                return [i, nums[i + 1:].index(target_pair) + i + 1]

            except:
                continue