class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[]
        for i in range(len(arr)-1):
            val=max(arr[i+1:])
            ans.append(val)
            arr[i]=-100
        ans.append(-1)
        return ans