class Solution:
    def scoreOfString(self, s: str) -> int:
        arr=[]
        val=0
        for i in range(len(s)-1,0,-1):
            val+=(abs(ord(s[i])-ord(s[i-1])))
            print(abs(ord(s[i])-ord(s[i-1])))
        return val


        