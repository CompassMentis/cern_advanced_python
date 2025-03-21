class Demo:
    def __init__(self):
        self.some_public_value = 5
        self._some_private_ish_value = 6
        self.__more_private_value = 7

    def change_values(self):
        self.some_public_value += 1
        self._some_private_ish_value += 1
        self.__more_private_value += 1


demo = Demo()
demo.change_values()
print(demo.some_public_value)  # 6
print(demo._some_private_ish_value)  # 7
print(demo._Demo__more_private_value)  # 9


print(demo.__more_private_value)
# AttributeError: 'Demo' object has no attribute '__more_private_value'.
# Did you mean: '_Demo__more_private_value'?
