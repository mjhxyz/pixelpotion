import os
from collections import namedtuple
import re

from PIL import Image


mode = '(1|2|3|4|5)'
w = '\d{1,4}'
h = '\d{1,4}'
image_format = '(jpeg|jpg|png)'
interlace = '[^/]+'
q = '\d{1,3}'
num_colors = '\d{1,3}'
ignore_error = '[^/]+'

fields_dict = {
    'mode': {'default': 1, 'type': str},
    'w': {'default': 0, 'type': int},
    'h': {'default': 0, 'type': int},
    'image_format': {'default': 'jpg', 'type': str},
    'interlace': {'default': 0, 'type': int},
    'q': {'default': 100, 'type': int},
    'num_colors': {'default': 128, 'type': int},
    'ignore_error': {'default': 0, 'type': int},
}

header_patttern = r'^image/' + fr'(?P<mode>{mode})/'

optional_fields_pattern = (
    fr'(/format/(?P<image_format>{image_format}))?'
    r'(/interlace/(?P<interlace>[^/]+))?'
    r'(/q/(?P<q>\d+))?'
    r'(/colors/(?P<num_colors>\d+))?'
    r'(/ignore_error/(?P<ignore_error>[^/]+))?'
)

image_p = (
    fr'{header_patttern}'
    fr'w/(?P<w>{w})/'
    fr'h/(?P<h>{h})'
    f'{optional_fields_pattern}'
    r'$'
)

image_p2 = (
    fr'{header_patttern}'
    fr'(w/(?P<w>{w})|h/(?P<h>{h}))'
    f'{optional_fields_pattern}'
    r'$'
)

ImageData = namedtuple(
    'ImageData',
    ['mode', 'w', 'h', 'image_format',
     'interlace', 'q', 'num_colors', 'ignore_error'
     ])


class Routes:
    def __init__(self):
        self.routes = []

    def add_route(self, route):
        self.routes.append(route)

    def get_or_default(self, **kwargs):
        for key, value in kwargs.items():
            if value is None:
                kwargs[key] = fields_dict[key]['default']
            else:
                kwargs[key] = fields_dict[key]['type'](value)
        return kwargs

    def route(self, *patterns):
        def decorator(func):
            def wrapper(d, input_file, output_file):
                d = ImageData(**self.get_or_default(**d))
                return func(d, input_file, output_file)
            self.add_route((patterns, wrapper))
            return func
        return decorator

    def match(self, path):
        for patterns, func in self.routes:
            for pattern in patterns:
                match = re.match(pattern, path)
                if match:
                    return func, match.groupdict()
        return None, None


def convert(path, input, output):
    func, data = routes.match(path)
    if not func:
        return False
    func(data, input_file=input, output_file=output)


routes = Routes()


@routes.route(image_p, image_p2)
def mode1handler(d, input_file, output_file):
    with Image.open(input_file) as img:
        if d.image_format is None:
            d.image_format = img.format
        w = d.w
        h = d.h

        if not w and not h:
            w, h = img.size
        elif w and not h:
            h = int(w / img.width * img.height)
        elif h and not w:
            w = int(h / img.height * img.width)
        else:
            pass

        if w > img.width:
            w = img.width
        if h > img.height:
            h = img.height
        # 居中裁剪后的矩形
        rect = (img.width - w) / 2, (img.height - h) / \
            2, (img.width + w) / 2, (img.height + h) / 2

        # img = img.resize((w, h))
        img = img.crop(rect)

        img.save(output_file, format=d.image_format, quality=d.q)


path = 'image/1/w/100/format/jpeg/interlace/1/q/90/colors/2/ignore_error/1'
convert(path, 'tmp/test.png', 'tmp/test.jpg')
