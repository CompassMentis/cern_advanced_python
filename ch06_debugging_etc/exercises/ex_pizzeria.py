# Here is a small part of what may be a solution to the pizzeria challenge from Chapter 4

# Todo: Some of the orders are incorrect. Run the code and see where it raises the first exception
#   Work out why it goes wrong, print a suitable error message and move on
#   The error message should state what (probably) went wrong,
#       and give a suggestion for how to fix it

# Todo: Repeat the above until all exceptions are handled

import pathlib


def load_crust_numbers():
    crusts = pathlib.Path('../data/pizza_crusts.txt').read_text().strip().split('\n')
    return {crust:number for (number, crust) in enumerate(crusts)}


def process_order(order, crust_numbers):
    customer, pizza_type, crust, number_of_pizzas = [part.strip() for part in order.split(',')]
    crust_number = crust_numbers[crust]
    number_of_pizzas = int(number_of_pizzas)
    print(f'Processing {number_of_pizzas} pizza(s) {pizza_type} with crust {crust_number}')


crust_numbers = load_crust_numbers()
with open('../data/orders.txt') as input_file:
    for order in input_file:
        process_order(order, crust_numbers)
