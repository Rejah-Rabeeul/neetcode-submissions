class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for val in nums:
            dict[val] = dict.get(val, 0) + 1
        ans = sorted(dict, key = dict.get)[-1:-(k+1):-1]
        print(ans)
        return ans