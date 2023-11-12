class Pizza:
    def get_ingredients(self):
        print(f'Get: {self.ingredients}')

    def prepare_ingredients(self):
        print('Clean and chop the ingredients')

    def assemble(self):
        print('Put toppings on base')

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

    def in_oven(self):
        print('15 minutes in the oven')


pizza = MargheritaPizza()
pizza.cook()

# Output:
# Get: ['cheese']
# Clean and chop the ingredients
# Create a thin-crust base
# Put toppings on base
# 15 minutes in the oven
