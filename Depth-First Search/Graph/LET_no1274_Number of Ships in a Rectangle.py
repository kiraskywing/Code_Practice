# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
# class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        result = 0
        if topRight.x >= bottomLeft.x and topRight.y >= bottomLeft.y and sea.hasShips(topRight, bottomLeft):
            if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return 1

            m_x, m_y = (topRight.x + bottomLeft.x) // 2, (topRight.y + bottomLeft.y) // 2
            result += self.countShips(sea, Point(m_x, m_y), bottomLeft)
            result += self.countShips(sea, Point(m_x, topRight.y), Point(bottomLeft.x, m_y + 1))
            result += self.countShips(sea, Point(topRight.x, m_y), Point(m_x + 1, bottomLeft.y))
            result += self.countShips(sea, topRight, Point(m_x + 1, m_y + 1))

        return result