import numpy

class Polynomial(object):

    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        """Evaluate the polynomial."""
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s

    def __add__(self, other):
        """Return self + other as Polynomial object."""
        # Two cases:
        #
        # self: X X X X X X X
        # other: X X X
        #
        # or:
        #
        # self: X X X X X
        # other: X X X X X X X X
        # Start with the longest list and add in the other
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:] # copy!
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = other.coeff[:] # copy!
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)

    def __sub__(self, other):
        """Return self + other as Polynomial object."""
        # Two cases:
        #
        # self: X X X X X X X
        # other: X X X
        #
        # or:
        #
        # self: X X X X X
        # other: X X X X X X X X
        # Start with the longest list and subtract in the other
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:] # copy!
            for i in range(len(other.coeff)):
                result_coeff[i] -= other.coeff[i]
        else:
            result_coeff = other.coeff[:] # copy!
            #needed in order to account for the order of subtraction
            for ii in range(len(result_coeff)):
                result_coeff[ii]=-result_coeff[ii]
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)


    def __mul__(self, other):
        c = self.coeff

        d = other.coeff
        M = len(c) - 1
        N = len(d) - 1
        result_coeff = numpy.zeros(M + N + 1)
        for i in range(0, M + 1):
            for j in range(0, N + 1):
                result_coeff[i + j] += c[i] * d[j]
        return Polynomial(result_coeff)

    def differentiate(self):
        """Differentiate this polynomial in-place."""

        for i in range(1, len(self.coeff)):
            self.coeff[i - 1] = i * self.coeff[i]
        del self.coeff[-1]

    def derivative(self):
        """Copy this polynomial and return its derivative."""

        dpdx = Polynomial(self.coeff[:])  # make a copy
        dpdx.differentiate()
        return dpdx

def test_Polynomial():
    p1 = Polynomial([1, -1])
    p2 = Polynomial([0, 1, 0, 0, -6, -1])
    p3 = p2 - p1
    print(p3.coeff)

if __name__=='__main__':
    test_Polynomial()
