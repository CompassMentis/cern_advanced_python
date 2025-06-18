import abc


class Dish(abc.ABC):
    @abc.abstractmethod
    def ingredients(self):
        ...

    @abc.abstractmethod
    def cook(self):
        ...


class Pizza(Dish):
    def ingredients(self):
        return ['base', 'sauce', 'topping']

    def cook(self):
        return 'Put in the oven until cooked'


class Soup(Dish):
    def cook(self):
        return 'Boil until cooked'


pizza = Pizza()

dish = Dish()
# TypeError: Can't instantiate abstract class Dish with abstract methods cook, ingredients

soup = Soup()
# TypeError: Can't instantiate abstract class Soup with abstract method ingredients
