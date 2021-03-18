class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius, self.x, self.y = radius, x_center, y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        r = self.radius * sqrt(random.uniform(0, 1))
        theta = random.uniform(0, 2*pi)
        return [self.x + r * cos(theta), self.y + r * sin(theta)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()