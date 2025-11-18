class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n=len(bits)
        step=0
        while (step<n-1):
            if bits[step]==0:
                step+=1
            else:
                step+=2
        return step==n-1