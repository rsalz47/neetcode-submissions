class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Very similar to binary search, just now need to bin search over 
        # vertical arrays
        if len(matrix) == 0:
            return False
        if target < matrix[0][0] or matrix[-1][-1] < target:
            return False

        # find what row we should look in
        target_row = None
        lb = 0
        rb = len(matrix) - 1

        while lb <= rb:
            midpoint = (lb + rb) // 2
            if matrix[midpoint][0] <= target and target <= matrix[midpoint][-1]:
                target_row = matrix[midpoint]
                break
            if matrix[midpoint][-1] < target:
                lb = midpoint + 1
            else:
                rb = midpoint - 1
        
        if target_row != None:
            return True if self.bin_search(target_row, target) >= 0 else False
        return False

    def bin_search(self, nums, target):
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