class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values={}
        for key,val in enumerate(nums):
            item=target-val
            if item in values:
                return [values[item],key]
            values[val]=key