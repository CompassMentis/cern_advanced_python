class Animal:
    def __init__(self, name):
        self.name = name


class SwimMixin:
    def swim(self):
        print(f'{self.name} swims')


class FlyMixin:
    def fly(self):
        print(f'{self.name} flies')


class Bird(FlyMixin, Animal):
    ...


class FlyingFish(FlyMixin, SwimMixin, Animal):
    ...


sky_glider = FlyingFish('SkyGlider')
sky_glider.fly()   # SkyGlider flies
sky_glider.swim()  # SkyGlider swims
