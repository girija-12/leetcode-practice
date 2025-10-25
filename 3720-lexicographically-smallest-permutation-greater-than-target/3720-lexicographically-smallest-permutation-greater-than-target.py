from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = Counter(s)
        sorted_chars = sorted(freq.keys())
        res = []
        
        def dfs(i, equal_prefix):
            if i == n:
                candidate = ''.join(res)
                return candidate if candidate > target else None
            
            for ch in sorted_chars:
                if freq[ch] == 0:
                    continue
                if equal_prefix and ch < target[i]:
                    continue
                if equal_prefix and ch > target[i]:
                    freq[ch] -= 1
                    remaining = []
                    for c in sorted_chars:
                        remaining.extend([c]*freq[c])
                    return ''.join(res + [ch] + remaining)
                freq[ch] -= 1
                res.append(ch)
                next_equal_prefix = equal_prefix and (ch == target[i])
                result = dfs(i + 1, next_equal_prefix)
                if result:
                    return result
                freq[ch] += 1
                res.pop()
            
            return None
        
        ans = dfs(0, True)
        return ans if ans else ""