# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        max = 0 
        for pi in points:
            max_temp = 0
            same_element = 0
            slopes = dict()
            for pj in points:
                slope = 0
                if pi.y == pj.y and pi.x == pj.x:
                    same_element = same_element + 1 
                    continue
                if pi.y == pj.y :
                    slope = 0
                elif pi.x == pj.x:
                    slope = float("inf")
                else:
                    slope = (pi.y-pj.y)/(pi.x-pj.x+0.0)
                count = slopes.get(slope, 0) + 1 
                slopes.update({slope:count})
                if count > max_temp:
                    max_temp = count
            max_temp = max_temp + same_element
            if max < max_temp:
                max = max_temp
                    
        return max
