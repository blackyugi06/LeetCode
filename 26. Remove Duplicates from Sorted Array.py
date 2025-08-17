class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        prev = nums[0]
        for i, c in enumerate(nums[1:]):
            if c != prev:
                nums[k] = c
                k += 1
            prev = c
        return k
        
