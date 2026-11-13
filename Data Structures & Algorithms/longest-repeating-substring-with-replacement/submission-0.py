class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans=0
        count = {}
        freq = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0) + 1
            freq = max(count[s[right]],freq)
            while((right-left+1) - freq > k):
                count[s[left]]-=1
                left+=1
            ans = max(ans,right-left+1)
        return ans