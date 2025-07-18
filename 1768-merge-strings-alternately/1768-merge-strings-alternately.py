class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res =''
        n1,n2=len(word1),len(word2)
        for i in range(max(n1,n2)):
            if i<n1:res+=word1[i]
            if i<n2:res+=word2[i]
        return res