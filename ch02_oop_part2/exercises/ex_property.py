# Todo: Add a property to this class called volume_in_fluid_ounces
#   which returns the volume in fluid ounces
#   where volume in fluid ounces = 35.195 * volume in litres

class Container:
    def __init__(self, volume_in_litres):
        self.volume_in_litres = volume_in_litres


milk_carton = Container(0.5)
print('Volume in litres', milk_carton.volume_in_litres)
print('Volume in fluid ounces', milk_carton.volume_in_fluid_ounces)
