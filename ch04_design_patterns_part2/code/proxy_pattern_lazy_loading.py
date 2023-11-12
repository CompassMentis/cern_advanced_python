import time
import random

from PIL import Image as pil_image
from PIL import ImageShow

# Show output using ImageMagick display command
# Remove to use your system's default image viewer
ImageShow.register(ImageShow.DisplayViewer(), 0)


class Image:
    def __init__(self, name):
        self.name = name
        self._image = None

    @staticmethod
    def load_picture_slowly(name):
        time.sleep(3)
        image = pil_image.open(name)
        image.load()
        return image

    @property
    def image(self):
        if self._image is None:
            self._image = self.load_picture_slowly(self.name)
        return self._image

    def show(self):
        self.image.show(title='eog')


images = [
    Image(f'images/image{i:02}.png')
    for i in range(1, 11)
]

for _ in range(2):
    random.choice(images).show()
