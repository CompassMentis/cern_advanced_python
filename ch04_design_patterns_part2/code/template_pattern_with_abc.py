import abc


class Pizza(abc.ABC):
    def get_ingredients(self):
        print(f'Get: {self.ingredients}')

    def prepare_ingredients(self):
        print('Clean and chop the ingredients')

    @abc.abstractmethod
    def prepare_base(self):
        ...

    def assemble(self):
        print('Put toppings on base')

    @abc.abstractmethod
    def in_oven(self):
        ...

    def cook(self):
        self.get_ingredients()
        self.prepare_ingredients()
        self.prepare_base()
        self.assemble()
        self.in_oven()


class MargheritaPizza(Pizza):
    ingredients = ['cheese']

    def prepare_base(self):
        print('Create a thin-crust base')


pizza = MargheritaPizza()
# TypeError: Can't instantiate abstract class MargheritaPizza
# with abstract method in_oven

pizza.cook()
