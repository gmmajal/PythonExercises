
class Account(object):
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.transactions=0

    def deposit(self, amount):
        self.balance += amount
        self.transactions+=1

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions += 1

    def dump(self):
        s = '%s, %s, balance: %s, no. of transactions:%d' % \
            (self.name, self.no, self.balance, self.transactions)
        print (s)


def test_Account():
    a=Account(name='John Doe', account_number='1234567',initial_amount=14000)
    a.deposit(200)
    a.withdraw(1000)
    a.withdraw(500)
    a.deposit(900)
    a.dump()

if __name__=='__main__':
    test_Account()