import math as math

class Vec2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other,(list,tuple)):
            other=Vec2D(other[0],other[1])
            return Vec2D(self.x + other.x, self.y + other.y)
        else:
            return Vec2D(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        return self.__add__(other)
    def __sub__(self, other):
        if isinstance(other,(list,tuple)):
            other=Vec2D(other[0],other[1])
            return Vec2D(self.x - other.x, self.y - other.y)
        else:
            return Vec2D(self.x - other.x, self.y - other.y)
    def __rsub__(self, other):
        if isinstance(other, (list, tuple)):
            other=Vec2D(other[0],other[1])
            return other.__sub__(self)
    def __mul__(self, other):
        if isinstance(other, (list,tuple)):
            other=Vec2D(other[0],other[1])
            return self.x*other.x + self.y*other.y
        else:
            return self.x * other.x + self.y * other.y
    def __rmul__(self, other):
        if isinstance(other, (list,tuple)):
            other=Vec2D(other[0],other[1])
            return self.__mul__(other)
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
    def __ne__(self, other):
        return not self.__eq__(other) # reuse __eq__


def main():
    u = Vec2D(-2, 4)
    v =  u+(1, 1.5)
    w = [-3, 2] + v
    print(w)
    vv=[-3,2]-w
    print(vv)
    uu=vv-(1,1.5)
    print(uu)
    zz=[1,2]*u
    print(zz)


if __name__=='__main__':
    main()