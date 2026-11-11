class Solution:
    def isPalindrome(self, s: str) -> bool:
        p="".join(char for char in s if char.isalnum())
        text=p.lower()
        return text==text[::-1]