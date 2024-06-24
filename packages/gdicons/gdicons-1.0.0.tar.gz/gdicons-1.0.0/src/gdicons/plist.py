import xml.etree.ElementTree as ET
from PIL import Image

def parse_array(element):
    text = element.text
    parentheses = text.replace("{", "(").replace("}", ")")

    return eval(parentheses)

def parse_sprite_data(sprite_data):
    sprite_offset = ()
    sprite_texture_rect = ()
    sprite_source_size = ()
    sprite_rotated = False

    for i, element in enumerate(sprite_data):
        if element.text == "spriteOffset":
            sprite_offset = parse_array(sprite_data[i + 1])

        elif element.text == "textureRect":
            sprite_texture_rect = parse_array(sprite_data[i + 1])

        elif element.text == "spriteSourceSize":
            sprite_source_size = parse_array(sprite_data[i + 1])

        elif element.text == "textureRotated":
            sprite_rotated = eval(sprite_data[i + 1].tag.title())

    corner = sprite_texture_rect[0]
    size = sprite_texture_rect[1]
    if sprite_rotated:
        size = size[::-1]
    sprite_texture_rect = (*corner, corner[0] + size[0], corner[1] + size[1])

    return {
        "offset": sprite_offset,
        "texture_rect": sprite_texture_rect,
        "source_size": sprite_source_size,
        "rotated": sprite_rotated
    }

def split_spritesheet(image_path, plist_path):
    spritesheet = Image.open(image_path).convert("RGBA")

    root = ET.parse(plist_path).getroot()
    sprites = root[0][1]

    split_sprites = {}
    texture_name = ""
    for element in sprites:
        if element.tag == "key":
            texture_name = element.text

        else:
            sprite_data = parse_sprite_data(element)

            sprite_image = spritesheet.crop(sprite_data["texture_rect"])
            if sprite_data["rotated"]:
                sprite_image = sprite_image.rotate(90, expand=True)

            sprite_image = sprite_image.crop(sprite_image.getbbox())

            split_sprites[texture_name] = {
                "image": sprite_image,
                "offset": sprite_data["offset"]
            }

    return split_sprites

def parse_animdesc_sprite(animdesc_element):
    sprite_animdesc = {}

    key = ""
    for element in animdesc_element:
        if element.tag == "key":
            key = element.text

        else:
            if key == "position":
                sprite_animdesc["position"] = parse_array(element)

            elif key == "rotation":
                sprite_animdesc["rotation"] = float(element.text)

            elif key == "scale":
                sprite_animdesc["scale"] = parse_array(element)

            elif key == "flipped":
                sprite_animdesc["flipped"] = parse_array(element)

    return sprite_animdesc

def parse_animdesc(target_element):
    animdesc = {}

    for i, element in enumerate(target_element):
        if element.tag == "key":
            tag = int(element.text[7:])
            animdesc_element = target_element[i + 1]

            animdesc.update({
                tag: parse_animdesc_sprite(animdesc_element)
            })

    return animdesc

def get_animdesc(plist_path, animation_frame):
    with open(plist_path) as file:
        root = ET.fromstring(file.read().strip())

    root = root[0][3]

    for i, element in enumerate(root):
        if element.text.startswith(animation_frame):
            target_element = root[i + 1]
            break

    return parse_animdesc(target_element)
