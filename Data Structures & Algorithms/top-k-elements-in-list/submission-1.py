class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for val in nums:
            dict[val] = dict.get(val, 0) + 1
        ans = sorted(dict, key = dict.get, reverse = True)[:k]
        print(ans)
        return ans