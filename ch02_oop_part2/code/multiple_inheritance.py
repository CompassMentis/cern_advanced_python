class Fish:
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(f'{self.name} swims')


class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f'{self.name} flies')


class FlyingFish(Fish, Bird):
    ...


sky_glider = FlyingFish('SkyGlider')
sky_glider.fly()   # SkyGlider flies
sky_glider.swim()  # SkyGlider swims
