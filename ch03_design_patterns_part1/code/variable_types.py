def create_demo(x):
    z = 5

    def demo(name):
        nonlocal z
        print(name, x)
        print('Local variables', locals())
    return demo


y = 10
demo = create_demo(y)
demo('Zoe')

print(f'Globals, {globals() = }')
for name, cell in zip(demo.__code__.co_freevars, demo.__closure__):
    print(f'Free variable {name} = {cell.cell_contents}')
