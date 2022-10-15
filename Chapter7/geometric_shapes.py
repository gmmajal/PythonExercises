from math import pi,sqrt


class Circle(object):
    def __init__(self, x0, y0, R):
        self.x0, self.y0, self.R = x0, y0, R

    def area(self):
        return pi*self.R**2

    def circumference(self):
        return 2*pi*self.R

class Triangle(object):

    def __init__(self, v1, v2, v3):
        self._v1, self._v2, self._v3 = v1, v2, v3

    def area(self):
        x1=self._v1[0]
        x2=self._v2[0]
        x3=self._v3[0]
        y1=self._v1[1]
        y2=self._v2[1]
        y3=self._v3[1]

        return 0.5*abs((x2*y3) - (x3*y2) - (x1*y3) + (x3*y1) + (x1*y2) - (x2*y1) )

    def perimeter(self):
        x1 = self._v1[0]
        x2 = self._v2[0]
        x3 = self._v3[0]
        y1 = self._v1[1]
        y2 = self._v2[1]
        y3 = self._v3[1]

        #length of each side
        d12=sqrt((x1-x2)**2+(y1-y2)**2)
        d23=sqrt((x2-x3)**2+(y2-y3)**2)
        d13=sqrt((x1-x3)**2+(y1-y3)**2)

        return d12+d23+d13


class Rectangle(object):

    def __init__(self, x0, W, H):
        self._x0, self._W, self._H = x0, W, H

    def area(self):
        return self._W*self._H

    def perimeter(self):
        return 2 * (self._W + self._H)


def test_Rectangle():
    v1=(0,0); H=2 ;W=3
    r=Rectangle(v1,W,H)
    expected=6
    computed=r.area()
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = 'computed area = % g != % g(expected)' % \
          (computed, expected)
    assert success, msg

    expected = 10
    computed = r.perimeter()
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = 'computed perimeter = % g != % g(expected)' % \
          (computed, expected)
    assert success, msg


def test_Triangle():
    v1 = (0, 0);v2 = (1, 0);v3 = (0, 2)
    t=Triangle(v1,v2,v3)
    vertices = [v1, v2, v3]
    expected = 1
    computed = t.area()
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = 'computed area = % g != % g(expected)' % \
            (computed, expected)
    assert success, msg

    expected = 3+sqrt(5)
    computed = t.perimeter()
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = 'computed perimeter = % g != % g(expected)' % \
          (computed, expected)
    assert success, msg

def test_Circle():
    R = 2.5
    c = Circle(7.4, -8.1, R)
    from math import pi
    expected_area = pi*R**2
    computed_area = c.area()
    diff = abs(expected_area - computed_area)
    tol = 1E-14
    assert diff < tol, 'bug in Circle.area, diff=%s' % diff
    expected_circumference = 2*pi*R
    computed_circumference = c.circumference()
    diff = abs(expected_circumference - computed_circumference)
    assert diff < tol, 'bug in Circle.circumference, diff=%f' % diff


if __name__=='__main__':
    test_Circle()
    test_Triangle()
    test_Rectangle()