from PIL import Image

path_input = "assets/inputs/images"
path_output = "assets/outputs/images"


image = Image.open(f"{path_input}/input.png")
width, height = image.size
half_width = int(width * 0.5)
half_height = int(height * 0.5)
coords = []


def append_coord(x1, y1, x2, y2):
    coords.append([x1, y1, x2, y2])


data = [
    [0, 0, half_width, half_height],
    [half_width, 0, width, half_height],
    [0, half_height, half_width, height],
    [half_width, half_height, width, height],
]

for item in data:
    append_coord(*item)

for index, coord in enumerate(coords):
    file_name = f"{path_output}/cropped_{index + 1}.png"
    cropped_image = image.crop((tuple(coord)))
    cropped_image.save(file_name)
