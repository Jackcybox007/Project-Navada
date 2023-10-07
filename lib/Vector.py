import math

class Vector2:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self,other):
        if not isinstance(other,Vector2):
            self.x *= other
            self.y *= other
        elif isinstance(other,Vector2):
            self.x *= other.x
            self.y *= other.y
        else:
            pass

        return Vector2(self.x, self.y)
    
    def __div__(self,other):
        if not isinstance(other, Vector2):
            self.x /= other
            self.y /= other
        else:
            pass
    
        return Vector2(self.x, self.y)


    def length(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    def normalize(self):
        return Vector2(self.x/self.length(), self.y/self.length())
    
if __name__ == "__main__":
    test = Vector2(0,0)