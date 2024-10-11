import pathlib

from PIL import Image
from PIL import ImageShow

# Show output using ImageMagick display command
# Remove to use your system's default image viewer
ImageShow.register(ImageShow.DisplayViewer(), 0)


def load_and_scale_image(path):
    image = Image.open(path)
    scale = min(256 / image.width, 256 / image.height)
    return image.resize((int(scale * image.width), int(scale * image.height)))


class ThumbnailImage:
    def __init__(self, path):
        self.image = load_and_scale_image(path)

    def show(self):
        self.image.show()


class BlackAndWhiteThumbnailImage(ThumbnailImage):
    def __init__(self, path):  # noqa
        self.image = load_and_scale_image(path).convert('L')


image_path = pathlib.Path.cwd() / 'images' / 'image11.png'
thumbnail = BlackAndWhiteThumbnailImage(image_path)
thumbnail.show()
