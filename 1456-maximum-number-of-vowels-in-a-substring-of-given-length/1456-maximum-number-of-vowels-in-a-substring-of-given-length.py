class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        curr = max_vowel = 0
        for i in range(len(s)):
            if s[i] in vowels:
                curr += 1
            if i >= k and s[i - k] in vowels:
                curr -= 1
            if i >= k - 1:
                max_vowel = max(max_vowel, curr)
        return max_vowel