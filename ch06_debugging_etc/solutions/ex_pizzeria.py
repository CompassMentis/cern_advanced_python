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
    try:
        customer, pizza_type, crust, number_of_pizzas = [part.strip() for part in order.split(',')]
    except ValueError:
        print('Incorrect order. Order should consist of "Customer Name, type of pizza, type of crust, number of pizzas')
        print(f'.. for order: {order}')
        return
    try:
        crust_number = crust_numbers[crust]
    except KeyError:
        print('Unknown crust type in order: {order}')
        print(f'.. Crust must be one of: {", ".join(crust_numbers.keys())}')
        return

    try:
        number_of_pizzas = int(number_of_pizzas)
    except ValueError:
        print(f'Incorrect number of pizzas in order: {order}')
        return
    print(f'Processing {number_of_pizzas} pizza(s) {pizza_type} with crust {crust_number}')


crust_numbers = load_crust_numbers()
with open('../data/orders.txt') as input_file:
    for order in input_file:
        process_order(order, crust_numbers)
