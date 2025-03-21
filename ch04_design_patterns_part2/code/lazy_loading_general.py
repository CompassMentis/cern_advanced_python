from PIL import Image

thumbnails = {}


def get_thumbnail(name):
    if name not in thumbnails:
        print(f'Loading {name}')
        image = Image.open(f'images/{name}.png')
        image.thumbnail(size=(200, 200))
        thumbnails[name] = image
    return thumbnails[name]


image = get_thumbnail('image01')
# Loading image01

image = get_thumbnail('image01')
# (no output - already loaded)
