

class Line(object):

    def __init__(self,p1,p2):
        x0 = p1[0]
        x1 = p2[0]
        y0 = p1[1]
        y1 = p2[1]
        self._a = (y1 - y0) / float(x1 - x0)
        self._b = y0 - self._a * x0

    def value(self,x):
        return self._a*x+self._b


def test_Line():
    p1=(2,3)
    p2=(7,5)
    l=Line(p1,p2)
    exp_val=13.0/5
    comp_val=l.value(1)
    diff = abs(exp_val - comp_val)
    tol = 1E-14
    assert diff < tol, 'bug in Line.value, diff=%f' % diff

    p1=[2,3]
    p2 = [7, 5]
    l = Line(p1, p2)
    exp_val = 13.0 / 5
    comp_val = l.value(1)
    diff = abs(exp_val - comp_val)
    tol = 1E-14
    assert diff < tol, 'bug in Line.value, diff=%f' % diff

if __name__=='__main__':
    test_Line()