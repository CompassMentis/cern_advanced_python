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
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.group = None

    def copy(self):
        result = Point(self.x, self.y)
        result.group = self.group
        return result

    def __repr__(self):
        return f'Point({self.x}, {self.y}), group = {self.group}'

    def distance_to(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

    def closest_centre(self, centres):
        closest = None
        for centre in centres:
            if closest is None or self.distance_to(centre) < self.distance_to(closest):
                closest = centre
        return closest


def main():
    source_image = Image.open(SOURCE_FILE)
    points = []
    x = 0
    while x < source_image.width:
        y = 0
        while y < source_image.height:
            if source_image.getpixel((x, y)) != (255, 255, 255):
                points.append(Point(x, y))
            y += 1
        x += 1

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
            points_in_group = []
            for point in points:
                if point.group == group:
                    points_in_group.append(point)
            sum_x = 0
            for point in points_in_group:
                sum_x += point.x
            sum_y = 0
            for point in points_in_group:
                sum_y += point.y
            new_centre = Point(sum_x / len(points_in_group), sum_y / len(points_in_group))
            new_centre.group = group
            new_centres.append(new_centre)
        centres = new_centres

        new_image = Image.new('RGB', source_image.size, (255, 255, 255))
        for i in range(len(points)):
            point = points[i]
            new_image.putpixel((point.x, point.y), GROUP_COLOURS[point.group])
        images.append(new_image)
    images[0].save(TARGET_FILE, save_all=True, append_images=images[1:], duration=1000)


if __name__ == '__main__':
    main()
