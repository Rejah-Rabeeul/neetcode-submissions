class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0,len(heights)-1
        ans=0
        val=0
        while left<right:
            if heights[left]<heights[right]:
                val=heights[left]*(right-left)
                left+=1
            else:
                val=heights[right]*(right-left)
                right-=1
            ans=max(ans,val)
        return ans