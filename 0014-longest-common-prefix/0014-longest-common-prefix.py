class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=min(strs,key=len)
        res=""
        if s=="" or len(strs)==1:
            return s
        for i in range(len(s)+1):
            if all(st.startswith(s[:i]) for st in strs):
                res=s[:i]
        return res