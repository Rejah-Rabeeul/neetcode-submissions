class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        first=0
        for i in range(len(t)):
            if s[first]==t[i]:
                first+=1
                if len(s)==first:
                    return True
        return False