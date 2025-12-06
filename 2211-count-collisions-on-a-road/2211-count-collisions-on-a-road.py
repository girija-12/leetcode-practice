class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip("L").rstrip("R")
        return directions.count("R") + directions.count("L")