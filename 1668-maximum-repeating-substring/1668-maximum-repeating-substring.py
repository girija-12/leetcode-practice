class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # Time Complexity: O(n*m)
        n = len(sequence)
        k = 0
        temp = word
        while len(temp) <= n:
            if temp not in sequence:
                break
            k += 1
            temp += word
        return k
