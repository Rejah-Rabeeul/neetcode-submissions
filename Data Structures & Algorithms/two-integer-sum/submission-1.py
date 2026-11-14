class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for val in range(len(nums)):
            rest = target - nums[val]
            if rest in values:
                return [values[rest], val]
            else:
                values[nums[val]] = val