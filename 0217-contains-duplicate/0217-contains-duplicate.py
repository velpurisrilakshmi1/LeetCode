class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length_of_nums = len(nums)
        if len(set(nums)) != length_of_nums:
            return True
        return False
        