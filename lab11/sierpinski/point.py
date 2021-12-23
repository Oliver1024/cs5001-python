class Point:
    """A class named Point"""
    def __init__(self, x, y):
        """Initialize the class"""
        self.xCoord = x
        self.yCoord = y
    
    def getX(self):
        """Get x coordinate"""
        return self.xCoord
    
    def getY(self):
        """Get y coordinate"""
        return self.yCoord
    
    def midPoint(self, otherPoint):
        """Get the midpoint between any two points"""
        # The following 0 assignments are placeholders
        # to make the coe run. They need to be made to 
        # calculate the coordinates of the new midpoint.
        # ToDo  replace newX newY value to a formula
        newX = (self.getX() + otherPoint.getX()) / 2
        newY = (self.getY() + otherPoint.getY()) / 2
        return Point(newX, newY)
