# Todo: Read the code. Run the code and view data/filtered.png

# Todo: Look at the documentation for Pillow Filters
#   https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html

# Todo: Create one a subclass of FilterTestBase, similar to EmbossedFilterTest, applying a different filter
#   Run it, check filtered.png

# Todo: Look at the documentation for rotating images
#   https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.rotate

# Todo: Create another subclass of FilterTestBase, using the same filter or as different one as the previous one
#   And give it a final_step method which rotates the final_image by 180 degrees
#   Run it, check filtered.png


import pathlib

from PIL import Image
from PIL import ImageFilter


class FilterTestBase:
    target_image_size = 250
    black_and_white = False

    def __init__(self, image_paths, target_path):
        self.image_paths = image_paths
        self.target_path = target_path
        self.images = None
        self.final_image = None

    @staticmethod
    def scale_image(image, size):
        scale = max(size / image.width, size / image.height)
        return image.resize((
            int(scale * image.width),
            int(scale * image.height)
        ))

    def scale_images(self):
        self.images = [
            self.scale_image(image, self.target_image_size)
            for image in self.images
        ]

    @staticmethod
    def crop_image_to_square(image, size):
        left = (image.width - size) // 2
        top = (image.height - size) // 2
        return image.crop((left, top, left + size - 1, top + size - 1))

    def crop_images_to_squares(self):
        self.images = [
            self.crop_image_to_square(image, self.target_image_size)
            for image in self.images
        ]

    def convert_to_black_and_white(self):
        self.images = [image.convert('L') for image in self.images]

    def filter_images(self):
        self.images = [self.filter_image(image) for image in self.images]

    def combine_images(self):
        image_size = (self.target_image_size * 2, self.target_image_size * 2)
        format = 'L' if self.black_and_white else 'RGB'
        self.final_image = Image.new(format, image_size)
        for index, image in enumerate(self.images):
            row = index // 2
            column = index % 2
            x, y = row * self.target_image_size, column * self.target_image_size
            self.final_image.paste(image, (x, y))

    def final_step(self):
        ...

    def save_final_image(self):
        self.final_image.save(self.target_path)

    def run(self):
        self.images = [
            Image.open(path)
            for path in self.image_paths
        ]
        self.scale_images()
        self.crop_images_to_squares()
        if self.black_and_white:
            self.convert_to_black_and_white()
        self.filter_images()
        self.combine_images()
        self.final_step()
        self.save_final_image()


class NoFilterTest(FilterTestBase):
    def filter_image(self, image):
        return image


class BlackWhiteNoFilterTest(FilterTestBase):
    black_and_white = True

    def filter_image(self, image):
        return image


class EmbossedFilterTest(FilterTestBase):
    def filter_image(self, image):
        return image.filter(ImageFilter.EMBOSS)


class UpsideDownFilterTest(FilterTestBase):
    def filter_image(self, image):
        return image.filter(ImageFilter.FIND_EDGES)

    def final_step(self):
        self.final_image = self.final_image.rotate(180)


data_path = pathlib.Path.cwd() / 'data'

source_image_paths = [
    path for path in data_path.iterdir()
    if path.suffix == '.png' and 'filtered' not in path.stem
]
target_path = data_path / 'filtered.png'
# filter = NoFilterTest(source_image_paths, target_path)
# filter = BlackWhiteNoFilterTest(source_image_paths, target_path)
# filter_test = EmbossedFilterTest(source_image_paths, target_path)
filter_test = UpsideDownFilterTest(source_image_paths, target_path)
filter_test.run()
