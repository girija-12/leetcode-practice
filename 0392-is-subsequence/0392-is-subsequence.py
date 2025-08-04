class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1,n2=len(s), len(t)
        if n1>n2:
            return False
        elif s==t:
            return True
        else:
            i,j=0,0
            ans=[0]*n1
            while(i<n1 and j<n2):
                if s[i]==t[j]:
                    ans[i]=1
                    i+=1
                    j+=1
                else:
                    j+=1
            return True if i==n1 else False