class Point:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data
        
    def __repr__(self):
        return "({},{})".format(self.x, self.y)
