
class Line(object):

    def __init__(self,p1,p2):
        if isinstance(p1, (tuple, list)) and isinstance(p2, (float, int)):
            # p1 is a point and p2 is slope
            self.a = p2
            self.b = p1[1] - p2 * p1[0]
        elif isinstance(p1, (float, int)) and isinstance(p2, (tuple, list)):
            # p1 is a slope and p2 is point
            self.a = p1
            self.b = p2[1] - p1 * p2[0]
        elif isinstance(p1, (tuple, list)) and isinstance(p2, (tuple, list)):
            #p1 and p2 are points
            x0 = p1[0]
            x1 = p2[0]
            y0 = p1[1]
            y1 = p2[1]
            self.a = (y1 - y0) / float(x1 - x0)
            self.b = y0 - self.a * x0
        elif isinstance(p1, (float, int)) and isinstance(p2, (float, int)):
            #p1 is the slope and p2 is the interception of y-axis
            self.a=p1
            self.b=p2

    def value(self,x):
        return self.a*x+self.b


def test_Line():
    p1=(2,3)
    p2=(7,5)
    l=Line(p1,p2)
    exp_val=13.0/5
    comp_val=l.value(1)
    diff = abs(exp_val - comp_val)
    tol = 1E-14
    assert diff < tol, 'bug in Line.value, diff=%f' % diff

    p1 = [2, 3]
    p2 = [7, 5]
    l = Line(p1, p2)
    exp_val = 13.0 / 5
    comp_val = l.value(1)
    diff = abs(exp_val - comp_val)
    tol = 1E-14
    assert diff < tol, 'bug in Line.value, diff=%f' % diff

    p1= 2
    p2= 5.0
    l = Line(p1, p2)
    exp_val = 7.0
    comp_val = l.value(1)
    diff = abs(exp_val - comp_val)
    tol = 1E-14
    assert diff < tol, 'bug in Line.value, diff=%f' % diff

    p1 = (0,-1)
    p2 = 5.0
    l = Line(p1, p2)
    exp_val = 4
    comp_val = l.value(1)
    diff = abs(exp_val - comp_val)
    tol = 1E-14
    assert diff < tol, 'bug in Line.value, diff=%f' % diff

    p1 = 5.0
    p2 = [0, -1]
    l = Line(p1, p2)
    exp_val = 4
    comp_val = l.value(1)
    diff = abs(exp_val - comp_val)
    tol = 1E-14
    assert diff < tol, 'bug in Line.value, diff=%f' % diff

if __name__=='__main__':
    test_Line()
