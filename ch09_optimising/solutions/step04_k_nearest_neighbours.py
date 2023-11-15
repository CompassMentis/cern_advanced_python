"""
Fourth step

Profiling shows that distance_to_squared (still) takes up a lot of time, but I can't think of any improvements

closest_centre also takes up a fair bit of time. This looks like a candidate for using min(...)

Duration at start 2.4610118189993955
Duration at end 2.384698103000119

Profiling no longer shows any obvious next step
A lot of the time now goes to image processing, which can probably be improved by studying the Pillow library
"""
import timeit
import math

from PIL import Image

SOURCE_FILE = '../data/data_points.png'
TARGET_FILE = '../data/data_points_grouped.gif'
ITERATIONS = 100
K = 4
GROUP_COLOURS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255)
]


class Point:
    def __init__(self, x, y, group=None):
        self.x = x
        self.y = y
        self.group = group

    def copy(self):
        return Point(self.x, self.y, self.group)

    def __repr__(self):
        return f'Point({self.x}, {self.y}), group = {self.group}'

    def distance_to(self, point):
        return math.dist((self.x, self.y), (point.x, point.y))

    def closest_centre(self, centres):
        return min(centres, key=self.distance_to)


def main():
    source_image = Image.open(SOURCE_FILE)
    points = [
        Point(x, y)
        for x in range(source_image.width)
        for y in range(source_image.height)
        if source_image.getpixel((x, y)) != (255, 255, 255)
    ]

    centres = []
    for group, point in enumerate(points[:K]):
        centre_point = point.copy()
        centre_point.group = group
        centres.append(centre_point)

    print(centres)
    images = []
    for _ in range(ITERATIONS):
        for point in points:
            point.group = point.closest_centre(centres).group

        new_centres = []
        for group in range(K):
            points_in_group = [point for point in points if point.group == group]
            sum_x = sum([point.x for point in points_in_group])
            sum_y = sum([point.y for point in points_in_group])
            new_centre = Point(sum_x / len(points_in_group), sum_y / len(points_in_group))
            new_centre.group = group
            new_centres.append(new_centre)
        centres = new_centres

        new_image = Image.new('RGB', source_image.size, (255, 255, 255))
        for point in points:
            new_image.putpixel((point.x, point.y), GROUP_COLOURS[point.group])
        images.append(new_image)
    images[0].save(TARGET_FILE, save_all=True, append_images=images[1:], duration=1000)


if __name__ == '__main__':
    print(timeit.timeit('main()', number=10, globals=locals()))
    # main()
