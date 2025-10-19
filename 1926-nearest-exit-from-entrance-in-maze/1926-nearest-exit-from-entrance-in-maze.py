from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols=len(maze), len(maze[0])
        q=deque()
        q.append((entrance[0],entrance[1],0))
        maze[entrance[0]][entrance[1]]='+'
        direction=[(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            row, col, step=q.popleft()
            for dr, dc in direction:
                newRow=row+dr
                newCol=col+dc
                if 0<=newRow<rows and 0<=newCol<cols:
                    if maze[newRow][newCol]=='.':
                        if newRow in (0, rows-1) or newCol in (0, cols-1):
                            return step+1
                        maze[newRow][newCol]='+'
                        q.append((newRow,newCol, step+1))
        return -1