class Vector2D(object):

    # @param vec2d {Array or Matrix[Array or Matrix[int]]}
    def __init__(self, vec2d):
        self.row = 0
        self.col = 0
        self.matrix = vec2d

    # @return {int} a next element
    def next(self):
        self.col += 1
        return self.matrix[self.row][self.col - 1]

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        while self.row < len(self.matrix) and self.col >= len(self.matrix[self.row]):
            self.row += 1
            self.col = 0
        return self.row < len(self.matrix)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())