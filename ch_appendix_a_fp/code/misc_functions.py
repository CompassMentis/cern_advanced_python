names = ['Maura', 'Nicolas', 'Reggie', 'Rex', 'Leonel']

print(all([0, 1, 1, 1]))  # False
print(any([0, 1, 1, 1]))  # True

print(sum([0, 1, 1, 1]))  # 3

print(max([12, 3, -5, 20]))  # 20
print(max(names))  # Rex
print(max(names, key=len))  # Nicolas

print(min([12, 3, -5, 20]))  # -5

print(sorted(names, key=lambda name: name[-1]))
# ['Maura', 'Reggie', 'Leonel', 'Nicolas', 'Rex']
