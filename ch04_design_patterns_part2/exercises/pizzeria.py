import abc


class BasePizza(abc.ABC):
    def apply_standard_ingredient(self, ingredient):
        standard_ingredient_lines = dict(
            ham_pineapple_onions='Arrange ham slices, pineapple chunks, and thinly sliced red onion on top of the cheese',
            pepperoni='Arrange pepperoni slices on top of the cheese',
            vegetables='Arrange sliced bell peppers, red onion, black olives, and mushrooms on top of the cheese',
            cook='Bake in the preheated oven for 10-12 minutes',
            cook_pepperoni='Bake in the preheated oven for 10-12 minutes or until the crust is golden and the pepperoni is crispy',
            olive_oil='Drizzle olive oil over the pizza and season with salt and pepper to taste',
            # preheat = 'Preheat your oven to 475°F (245°C)',
            # roll_out = 'Roll out the pizza dough into your desired shape and thickness',
            basil='Scatter fresh basil leaves on top of the cheese',
            chicken='Scatter shredded cooked chicken and thinly sliced red onion over the sauce',
            bbq_sauce='Spread a layer of BBQ sauce over the dough',
            tomato_sauce='Spread a thin layer of tomato sauce over the dough',
            mozzarella_over_sauce='Sprinkle mozzarella cheese evenly over the sauce',
            mozzarella_over_toppings='Sprinkle mozzarella cheese evenly over the toppings',
        )
        self.tell_cook(standard_ingredient_lines[ingredient])


    def tell_cook(self, message):
        print(message)

    def preheat_oven(self):
        self.tell_cook('Preheat your oven to 475°F (245°C)')

    def prepare_dough(self):
        self.tell_cook('Roll out the pizza dough into your desired shape and thickness')

    @abc.abstractmethod
    def add_sauce(self):
        ...

    @abc.abstractmethod
    def add_ingredients(self):
        ...

    @abc.abstractmethod
    def in_oven(self):
        ...


    def cook(self):
        self.preheat_oven()
        self.prepare_dough()
        self.add_sauce()
        self.add_ingredients()
        self.in_oven()


class MargheritaPizza(BasePizza):
    ingredients = [
        'Pizza dough',
        'Tomato sauce',
        'Mozzarella cheese',
        'Fresh basil leaves',
        'Olive oil',
        'Salt and pepper',
    ]

    def add_sauce(self):
        self.apply_standard_ingredient('tomato_sauce')

    def add_ingredients(self):
        for ingredient in ['mozzarella_over_sauce', 'basil', 'olive_oil']:
            self.apply_standard_ingredient(ingredient)

    def in_oven(self):
        self.apply_standard_ingredient('cook')


class PepperoniPizza(BasePizza):
    ingredients = [
        'Pizza dough',
        'Tomato sauce',
        'Mozzarella cheese',
        'Pepperoni slices',
    ]

    def add_sauce(self):
        self.apply_standard_ingredient('tomato_sauce')

    def add_ingredients(self):
        for ingredient in ['mozzarella_over_sauce', 'pepperoni']:
            self.apply_standard_ingredient(ingredient)

    def in_oven(self):
        self.apply_standard_ingredient('cook_pepperoni')


class BBQChickenPizza(BasePizza):
    ingredients = [
        'Pizza dough',
        'BBQ sauce',
        'Cooked chicken breast, shredded',
        'Red onion, thinly sliced',
        'Mozzarella cheese',
    ]

    def add_sauce(self):
        self.apply_standard_ingredient('bbq_sauce')

    def add_ingredients(self):
        for ingredient in ['chicken', 'mozzarella_over_toppings']:
            self.apply_standard_ingredient(ingredient)

    def in_oven(self):
        self.apply_standard_ingredient('cook')


class VegetarianSupremePizza(BasePizza):
    ingredients = [
        'Pizza dough',
        'Tomato sauce',
        'Mozzarella cheese',
        'Bell peppers (red, green, and yellow), sliced',
        'Red onion, thinly sliced',
        'Black olives, sliced',
        'Mushrooms, sliced',
    ]

    def add_sauce(self):
        self.apply_standard_ingredient('tomato_sauce')

    def add_ingredients(self):
        for ingredient in ['mozzarella_over_sauce', 'vegetables']:
            self.apply_standard_ingredient(ingredient)

    def in_oven(self):
        self.apply_standard_ingredient('cook')


class HawaiianPizza(BasePizza):
    ingredients = [
        'Pizza dough',
        'Tomato sauce',
        'Mozzarella cheese',
        'Ham slices',
        'Pineapple chunks',
        'Red onion, thinly sliced',
    ]

    def add_sauce(self):
        self.apply_standard_ingredient('tomato_sauce')

    def add_ingredients(self):
        for ingredient in ['mozzarella_over_sauce', 'ham_pineapple_onions']:
            self.apply_standard_ingredient(ingredient)

    def in_oven(self):
        self.apply_standard_ingredient('cook')


class StoreRoom:
    def __init__(self):
        self.stock_levels = {
            ingredient: 5
            for ingredient in self.get_unique_ingredients()
        }

    def get_unique_ingredients(self):
        ingredients = set()
        for object in globals().values():
            if isinstance(object, type) and issubclass(object, BasePizza) and object is not BasePizza:
                ingredients.update(object.ingredients)
        return ingredients


store_room = StoreRoom()
# print(store_room.stock_levels)

class Order:
    def __init__(self, customer, pizza_type, crust):
        self.customer = customer
        self.pizza_type = pizza_type
        self.crust = crust

    def __repr__(self):
        return f"Order('{self.customer}', '{self.pizza_type}', '{self.crust}')"

    def process(self):
        print(f'Processing {self}')


def process_orders():
    for line in open('data/orders.txt'):
        order = Order(*line.strip().split(', '))
        order.process()


process_orders()