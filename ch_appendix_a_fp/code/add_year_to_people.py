def aged_by_one(person):
    return (person[0], person[1] + 1)


people = [
    ('Olivia', 44),
    ('Liam', 21),
    ('Emma', 68),
    ('Noah', 27),
    ('Ava', 99)
]

older_people = [
    aged_by_one(person)
    for person in people
]

print(older_people)
# [('Olivia', 45), ('Liam', 22),
#  ('Emma', 69), ('Noah', 28), ('Ava', 100)]
