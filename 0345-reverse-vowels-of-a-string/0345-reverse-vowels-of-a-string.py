class Solution:
    def reverseVowels(self, s: str) -> str:
        arr=[x for x in s if x in 'aeiouAEIOU'][::-1]
        i, s = 0, list(s)
        for x in range(len(s)):
            if s[x] in arr:
                s[x]=arr[i]
                i+=1
        return "".join(s)