
class Hello(object):

    def __call__(self, args='World'):
        str='Hello, '+args+'!'
        return str

    def __str__(self):
        return 'Hello, World!'
