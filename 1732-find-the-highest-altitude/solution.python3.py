class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        
        altitude = 0 
        highest = 0
        for x in gain:
            altitude = altitude + x
            if(altitude >= highest):
                highest = altitude

        return highest