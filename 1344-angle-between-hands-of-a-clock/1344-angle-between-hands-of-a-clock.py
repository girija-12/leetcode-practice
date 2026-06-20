class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle=abs(minutes*6-((hour%12)*30+ 0.5*minutes))
        return min(angle, 360-angle)