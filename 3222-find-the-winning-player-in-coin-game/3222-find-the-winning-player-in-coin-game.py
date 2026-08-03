class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        winner="Bob"
        while x>0 and y>3:
            winner="Alice" if winner=="Bob" else "Bob"
            x-=1
            y-=4
        return winner