# coding: utf-8
import json
import os
import imghdr
import colorsys
from PIL import Image


def read_dir_img(dir, prefix):
    # Host for storing images
    img_host = prefix
    img_type = {'jpg', 'bmp', 'png', 'jpeg', 'rgb', 'tif'}
    json_data = {}
    json_data['msg'] = 'Success'
    json_data['Author'] = 'Stack Dev'
    json_data['Blog'] = 'https://stackblog.cf'
    json_data['data'] = []
    for path in os.listdir(dir):
        if imghdr.what(os.path.join(dir, path)) in img_type:
            item = {}
            item['title'] = os.path.basename(path)
            item['url'] = os.path.join(img_host, item['title'])
            item['size'] = hum_convert(
                os.path.getsize(os.path.join(dir, path)))
            item['width'], item['height'] = Image.open(
                os.path.join(dir, path)).size
            # item['color'] = get_dominant_colors(os.path.join(dir, path),1)[0]
            item['color'] = get_dominant_color(os.path.join(dir, path))
            json_data['data'].append(item)

    return json_data


def hum_convert(value):
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    size = 1024.0
    for i in range(len(units)):
        if (value / size) < 1:
            return "%.2f%s" % (value, units[i])
        value = value / size


def get_dominant_colors(path, len):
    image = Image.open(path)

    # compress pictures
    small_image = image.resize((80, 80))
    result = small_image.convert(
        "P", palette=Image.ADAPTIVE, colors=len
    )

    # get dominant colors
    palette = result.getpalette()
    color_counts = sorted(result.getcolors(), reverse=True)
    colors = list()

    for i in range(len):
        palette_index = color_counts[i][1]
        dominant_color = palette[palette_index * 3: palette_index * 3 + 3]
        colors.append(tuple(dominant_color))

    # print(colors)
    return colors


def get_dominant_color(path):
    image = Image.open(path)
    image = image.convert('RGBA')

    # Shrink the image, so we don't spend too long analysing color
    # frequencies. We're not interpolating so should be quick.
    image.thumbnail((200, 200))

    max_score = 0
    dominant_color = None

    for count, (r, g, b, a) in image.getcolors(image.size[0] * image.size[1]):
        # Skip 100% transparent pixels
        if a == 0:
            continue

        # Get color saturation, 0-1
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]

        # Calculate luminance - integer YUV conversion from
        # http://en.wikipedia.org/wiki/YUV
        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)

        # Rescale luminance from 16-235 to 0-1
        y = (y - 16.0) / (235 - 16)

        # Ignore the brightest colors
        if y > 0.9:
            continue

        # Calculate the score, preferring highly saturated colors.
        # Add 0.1 to the saturation so we don't completely ignore grayscale
        # colors by multiplying the count by zero, but still give them a low
        # weight.
        score = (saturation + 0.1) * count

        if score > max_score:
            max_score = score
            dominant_color = [r, g, b]

        return dominant_color


def write_json(data, dest):
    with open(os.path.join(dest, 'data.json'), 'w') as f:
        f.write(json.dumps(data))
        f.close()
    print('Output directory for JSON file: \033[1;32m{}\033[0m'.format(
        os.path.join(dest, 'data.json')))


if __name__ == '__main__':
    # File directory for images, /Users/xxx/Downloads/yyy
    dir_path = input('File directory for images:')
    # Prefix for generated links, https://xxx.yy
    prefix = input(
        'Prefix for generated links(For example, a host that stores images):')
    data = read_dir_img(dir_path, prefix)
    write_json(data, dir_path)
