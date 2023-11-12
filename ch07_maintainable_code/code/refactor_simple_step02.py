def compute_area(radius):
    return 3.14 * (radius**2)


for i in range(1, 5):
    area = compute_area(i)
    print("area is {0:0.2f}".format(area))
