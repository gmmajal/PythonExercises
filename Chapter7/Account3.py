import datetime


class AccountP(object):
    def __init__(self, name, account_number, initial_amount):
        self._name = name
        self._no = account_number
        self._transactions=[{'initial amount':initial_amount,'datetime':datetime.datetime.now()}]

    def deposit(self, amount):
        d={'deposit amount':amount,'datetime':datetime.datetime.now()}
        self._transactions.append(d)

    def withdraw(self, amount):
        d = {'withdraw amount': amount, 'datetime': datetime.datetime.now()}
        self._transactions.append(d)

    def get_balance(self):
        initial_amount=self._transactions[0]['initial amount']
        balance=initial_amount
        for i in range(1,len(self._transactions)):
            if 'deposit amount' in self._transactions[i]:
                balance += self._transactions[i]['deposit amount']
            elif 'withdraw amount' in self._transactions[i]:
                balance -= self._transactions[i]['withdraw amount']
        return balance

    def dump(self):
        s = '%s, %s, balance: %s' % \
        (self._name, self._no, self.get_balance())
        print (s)

    def print_transactions(self):
        for i in self._transactions:
            dict_key=list(i.keys())
            dict_value=list(i.values())
            print('{:<20} {:<15} {:<10} {:<40}'.format(dict_key[0],dict_value[0], dict_key[1],str(dict_value[1])))


def test_AccountP():
    a=AccountP(name='John Doe', account_number='1234567',initial_amount=14000)
    a.deposit(200)
    a.withdraw(1000)
    a.withdraw(500)
    a.deposit(900)
    a.dump()
    a.print_transactions()

if __name__=='__main__':
    test_AccountP()