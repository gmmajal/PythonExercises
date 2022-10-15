
class Account(object):

    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def __iadd__(self, amount):
        return Account(self.name,self.no,self.balance+amount)

    def __isub__(self, amount):
        return Account(self.name,self.no,self.balance-amount)

    def __str__(self):
        s = '%s, %s, balance: %f' % (self.name, self.no, self.balance)
        return s

    def __repr__(self):
         s = '%s, %s, balance: %f' % (self.name, self.no, self.balance)
         return s


def test_Account():
    a = Account(name='John Doe', account_number='1234567', initial_amount=14000)
    a += 200
    a -= 1000
    a -= 500
    a += 900
    print (a)


if __name__=='__main__':
    test_Account()