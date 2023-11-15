import dataclasses


# TODO: Create a dataclass called CoachTrip with the following attributes:
#   departure_city, destination_city, number_of_passengers, length_in_miles, is_one_way
@dataclasses.dataclass
class CoachTrip:
    departure_city: str
    destination_city: str
    number_of_passengers: int
    length_in_miles: float
    is_one_way: bool

# TODO: Create two instances of the dataclass
trip1 = CoachTrip('Berlin', 'Prague', 5, 73.1, True)
trip2 = CoachTrip('Leiden', 'Geneva', 10, 400.1, False)


# TODO: Use print(class_name) to print out both instances
print(trip1)
print(trip2)

# TODO: Change the number_of_passengers for one of the instances
#   and print(class_name) again
trip1.number_of_passengers += 7
print(trip1)
