import random
from PIL import Image, ImageDraw

STRAWBERRY_MODEL = [
    [0, 0, 0, 2, 0, 0, 0],
    [0, 2, 2, 2, 2, 2, 0],
    [2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 0]
]

HEART_MODEL = [
    [0, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

def draw_shape(draw, model, start_x, start_y, p_size, default_color):
    colors = {
        1: default_color,
        2: (34, 139, 34),  # Зеленый (для хвостика клубники)
        3: (178, 34, 34)  # Темно-красный (для теней)
    }
    for r_idx, row in enumerate(model):
        for c_idx, value in enumerate(row):
            if value in colors:
                x = start_x + c_idx * p_size
                y = start_y + r_idx * p_size
                draw.rectangle([x, y, x + p_size - 1, y + p_size - 1], fill=colors[value])


def generate_visual_cipher(number, bit_length=16):
    key = random.getrandbits(bit_length)
    encrypted = number ^ key

    data_bits = [int(b) for b in bin(encrypted)[2:].zfill(bit_length)]
    key_bits = [int(b) for b in bin(key)[2:].zfill(bit_length)]

    img_w, img_h = 800, 500
    p_size = 6
    img = Image.new('RGB', (img_w, img_h), 'white')
    draw = ImageDraw.Draw(img)

    margin_top = 120
    col_spacing = 90
    row_spacing = 80

    for i in range(bit_length):
        row, col = i // 4, i % 4
        lx, rx = 70 + col * col_spacing, 420 + col * col_spacing
        ly = ry = margin_top + row * row_spacing

        # Левая часть (Данные)
        if data_bits[i] == 1:
            draw_shape(draw, HEART_MODEL, lx, ly, p_size, (255, 165, 0))
        else:
            draw_shape(draw, STRAWBERRY_MODEL, lx, ly, p_size, (255, 0, 0))

        # Правая часть (Ключ)
        if key_bits[i] == 1:
            draw_shape(draw, HEART_MODEL, rx, ry, p_size, (255, 165, 0))
        else:
            draw_shape(draw, STRAWBERRY_MODEL, rx, ry, p_size, (255, 0, 0))

    img.save("") # путь к папке для сохранения картинки

# Запуск
generate_visual_cipher(65535, 16)
