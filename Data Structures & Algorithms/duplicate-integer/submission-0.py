class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        conv_set = set(nums)
        return len(conv_set) != len(nums)