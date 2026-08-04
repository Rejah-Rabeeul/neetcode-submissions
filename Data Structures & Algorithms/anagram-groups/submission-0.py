class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        names={}
        for i in strs:
            val="".join(sorted(i))
            if val not in names:
                names[val]=[]
            names[val].append(i)
        return list(names.values())