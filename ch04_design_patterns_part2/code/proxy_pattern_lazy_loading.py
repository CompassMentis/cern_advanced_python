import time
import random

from PIL import Image as pil_image
from PIL import ImageShow

# Show output using ImageMagick display command
# Remove to use your system's default image viewer
ImageShow.register(ImageShow.DisplayViewer(), 0)


class Thumbnail:
    def __init__(self, name):
        self.name = name
        self._image = None

    @staticmethod
    def load_picture_slowly(name):
        time.sleep(3)
        image = pil_image.open(name)
        image.thumbnail(size=(200, 200))
        return image

    @property
    def image(self):
        if self._image is None:
            self._image = self.load_picture_slowly(self.name)
        return self._image

    def show(self):
        self.image.show(title='eog')


thumbnails = [
    Thumbnail(f'images/image{i:02}.png')
    for i in range(1, 11)
]

print("10 images 'created'")
for _ in range(2):
    random.choice(thumbnails).show()
