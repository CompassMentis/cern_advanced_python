class Fish:
    def swim(self):
        print('Swimming')


class Bird:
    def fly(self):
        print('Flying')


class FlyingFish:
    def __init__(self):
        self.fish = Fish()
        self.bird = Bird()

    def swim(self):
        self.fish.swim()

    def fly(self):
        self.bird.fly()


sky_glider = FlyingFish()
sky_glider.fly()   # Flying
sky_glider.swim()  # Swimming
