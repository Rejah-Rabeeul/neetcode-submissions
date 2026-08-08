class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occur={}
        for val in nums:
            if val not in occur.keys():
                occur[val]=0
            occur[val]+=1
        largest= sorted(occur, key=lambda i:occur[i], reverse=True)[:k]
        return largest
