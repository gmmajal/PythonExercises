
class Y(object):

    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81

    def __call__(self,t):
         return self.v0*t - 0.5*self.g*t**2
