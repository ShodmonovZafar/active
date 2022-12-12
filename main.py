class Polygon:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
    
    def getArea(self):
        pass
    
    def getPerimeter(self):
        pass

class Rectangle(Polygon):
    def __init__(self, height, width) -> None:
        super().__init__(height, width)
    
    def getArea(self):
        return self.height * self.width
    
    def getPerimeter(self):
        return 2 * (self.height + self.width)

class Square(Polygon):
    def __init__(self, width) -> None:
        super().__init__(width, width)
    
    def getArea(self):
        return self.height ** 2
    
    def getPerimeter(self):
        return self.height * 4

