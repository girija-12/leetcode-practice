class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k>len(s):
            return False
        subs=s[:k]
        seen={subs}
        for i in range(k,len(s)):
            subs=subs[1:]+s[i]
            seen.add(subs)
        return len(seen)==2**k