class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        hour_angle = 360 * (hour + minutes / 60) / 12
        minute_angle = 360 * minutes / 60
        
        return min(abs(hour_angle - minute_angle), 
                   abs((360 + hour_angle) - minute_angle), 
                   abs(hour_angle - (minute_angle + 360)))