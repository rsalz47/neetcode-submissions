class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search works by constantly splitting the structure into halves
        # leverages the fact that it is sorted so we always have a half to hone in on
        if len(nums) == 0:
            return -1
        lb = 0
        rb = len(nums) - 1
        
        while lb <= rb:
            midpoint = (lb + rb) // 2

            if nums[midpoint] == target:
                return midpoint
            if target < nums[midpoint]:
                rb = midpoint - 1
            elif nums[midpoint] < target:
                lb = midpoint + 1
        return -1