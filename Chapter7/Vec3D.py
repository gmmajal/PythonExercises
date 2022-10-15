import math as math

class Vec3D(object):
    def __init__(self, x, y , z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        if isinstance(other,(list,tuple)):
            other=Vec3D(other[0],other[1], other[2])
            return Vec3D(self.x + other.x, self.y + other.y, self.z+ other.z)
        else:
            return Vec3D(self.x + other.x, self.y + other.y, self.z+ other.z)

    def __radd__(self, other):
        return self.__add__(other)
    def __sub__(self, other):
        if isinstance(other,(list,tuple)):
            other=Vec3D(other[0],other[1], other[2])
            return Vec3D(self.x - other.x, self.y - other.y, self.z- other.z)
        else:
            return Vec3D(self.x - other.x, self.y - other.y, self.z- other.z)
    def __rsub__(self, other):
        if isinstance(other, (list, tuple)):
            other=Vec3D(other[0],other[1],other[2])
            return other.__sub__(self)
    def __mul__(self, other):
        if isinstance(other, (list,tuple)):
            other=Vec3D(other[0],other[1],other[2])
            return self.x*other.x + self.y*other.y+self.z*other.z
        else:
            return self.x * other.x + self.y * other.y+self.z*other.z
    def __rmul__(self, other):
        if isinstance(other, (list,tuple)):
            other=Vec3D(other[0],other[1],other[2])
            return self.__mul__(other)
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z==other.z
    def __str__(self):
        return '(%g, %g, %g)' % (self.x, self.y, self.z)
    def __ne__(self, other):
        return not self.__eq__(other) # reuse __eq__
    def cross(self,other):
        x1 = self.y*other.z-self.z*other.y
        x2 = self.z*other.x-self.x*other.z
        x3 = self.x*other.y -self.y*other.x
        return Vec3D(x1,x2,x3)

def test_block():
    v=Vec3D(1,2,3)
    u=v.cross(v)
    print(u)

if __name__=='__main__':
    test_block()