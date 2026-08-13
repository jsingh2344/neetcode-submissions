class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_version = set(nums)
        if not nums:
            return False
        if len(set_version) == len(nums):
            return False
        return True
        
