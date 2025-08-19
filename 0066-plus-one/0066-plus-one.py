class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=int(''.join([str(x) for x in digits]))+1
        return list(map(int, str(x)))