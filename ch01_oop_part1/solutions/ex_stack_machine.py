# Todo: Create a class 'StackMachine'
#   This will use a stack to do some simple calculations

# Todo: Create a __init__ method which creates a private list called _stack

# Todo: Create a push method which appends an item to the stack

# Todo: Create a pop method which removes the last item from the stack and returns it

# Todo: Create a one_calculation method which:
#   pops the top two items of the stack. This will be two numbers
#   pops the top of the stack. This will be the operator: +, -, * or /
#   ... we'll call these 'b' and 'a' (note: order is swapped between pushing and popping)
#   calculates a + b, a - b, a / b, or a * b, depending on the operator
#   and pushes the result back on to the stack

# Todo: Create a calculate method which:
#   Whilst there are > 1 elements on the stack, calls one_calculation
#   Once there is 1 element on the stack, takes it off the stack and prints it

# Todo: Note that there's a bonus exercise at the end

class StackMachine:
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def push_multiple(self, items):
        self._stack.extend(items)

    def pop(self):
        return self._stack.pop()

    def one_calculation(self):
        operators = (self.pop(), self.pop())
        operand = self.pop()

        if operand == '+':
            result = sum(operators)
        elif operand == '-':
            result = operators[1] - operators[0]
        elif operand == '*':
            result = operators[0] * operators[1]
        elif operand == '/':
            result = operators[1] / operators[0]
        self.push(result)

    def calculate(self):
        while len(self._stack) > 1:
            self.one_calculation()
        print(self.pop())


stack_machine = StackMachine()
stack_machine.push('+')
stack_machine.push(1)
stack_machine.push(5)
stack_machine.calculate()
# Expected output: 6 (1 + 5)

# Todo (bonus): Create a push_multiple method
#   which takes a list or tuple of elements
#   and puts them all on the stack
stack_machine.push_multiple(['*', 3, '-', 5, 1])
stack_machine.calculate()
# Expected output: 12 (3 * (5 - 1))
