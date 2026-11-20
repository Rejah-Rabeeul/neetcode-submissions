class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = max(1, sum(piles)//h)
        right = max(piles)
        ans = float('inf')
        while left <= right:
            nums = 0
            mid = (left + right) // 2
            for val in piles:
                nums += (val + mid - 1 ) // mid
                if nums > h:
                    break
            if nums > h :
                left = mid + 1
            else:
                ans = min(ans, mid)
                right = mid - 1
        return ans