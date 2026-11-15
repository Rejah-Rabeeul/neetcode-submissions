class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, t1 = sorted(s), sorted(t)
        return True if s1 == t1 else False