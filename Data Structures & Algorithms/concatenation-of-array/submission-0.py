class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            val=nums[i]
            nums.append(val)
        return nums