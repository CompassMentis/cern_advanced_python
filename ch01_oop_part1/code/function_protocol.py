class AddSomething:
    def __init__(self, amount):
        self.amount = amount

    def __call__(self, number):
        return number + self.amount


add_five = AddSomething(5)
print(add_five(17))  # 22

