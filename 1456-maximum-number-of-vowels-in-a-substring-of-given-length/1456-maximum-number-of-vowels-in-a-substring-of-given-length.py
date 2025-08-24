class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n=len(s)
        def is_vowel(x):
            return x in {'a','e','i','o','u'}
        curr_vowel=sum([is_vowel(i) for i in s[:k]])
        max_vowel=curr_vowel
        for i in range(k,n):
            if is_vowel(s[i]):
                curr_vowel+=1
            if is_vowel(s[i-k]):
                curr_vowel-=1
            max_vowel=max(max_vowel,curr_vowel)
        return max_vowel