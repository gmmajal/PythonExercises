
class Rope(object):

    def __init__(self,knot):
        self.knot=knot

    def __add__(self, other):
        return self.knot+other.knot+1

    def __str__(self):
        return self.knot


def test_block():
    r1= Rope(1)
    r2= Rope(2)
    r3=r1+r2
    assert r3 == 4, "The addition of knots does not match"


if __name__=='__main__':
    test_block()