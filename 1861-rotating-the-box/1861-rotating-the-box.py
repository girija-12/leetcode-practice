class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n=len(boxGrid), len(boxGrid[0])
        for row in boxGrid:
            empty=n-1
            for i in range(n-1, -1, -1):
                if row[i]=='*':
                    empty=i-1
                elif row[i]=='#':
                    row[i]='.'
                    row[empty]='#'
                    empty-=1
        rotated=[['']*m for _ in range(n)]
        for r in range(m):
            for c in range(n):
                rotated[c][m-1-r]=boxGrid[r][c]
        return rotated