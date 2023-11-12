class Account:
    def __init__(self, name):
        self.name = name
        self._history = [0]

    @property
    def amount(self):
        return self._history[-1]

    @amount.setter
    def amount(self, new_value):
        self._history.append(new_value)

    @amount.deleter
    def amount(self):
        raise NotImplementedError

account = Account('My current account')
account.amount = 5
print(account.amount)   # 5
account.amount += 10
print(account.amount)   # 15
print(account._history)  # [0, 5, 15]

del account.amount  # NotImplementedError
