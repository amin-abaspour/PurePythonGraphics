
from debug import validate_pixel_matrix

def rgb_matrix_to_bmp(rgb_matrix):
    validate_pixel_matrix(rgb_matrix)  # Validate the input
    height, width = len(rgb_matrix), len(rgb_matrix[0])
    padding = (4 - (width * 3) % 4) % 4
    file_size = 14 + 40 + (3 * width + padding) * height
    bmp = bytearray()
    bmp += b'BM'
    bmp += file_size.to_bytes(4, 'little')
    bmp += (0).to_bytes(4, 'little')
    bmp += (14 + 40).to_bytes(4, 'little')
    bmp += (40).to_bytes(4, 'little')
    bmp += width.to_bytes(4, 'little')
    bmp += height.to_bytes(4, 'little')
    bmp += (1).to_bytes(2, 'little')
    bmp += (24).to_bytes(2, 'little')
    bmp += (0).to_bytes(4, 'little')
    bmp += ((3 * width + padding) * height).to_bytes(4, 'little')
    bmp += (0).to_bytes(4, 'little')
    bmp += (0).to_bytes(4, 'little')
    bmp += (0).to_bytes(4, 'little')
    bmp += (0).to_bytes(4, 'little')
    for row in reversed(rgb_matrix):
        for (r, g, b) in row:
            bmp += bytes([b, g, r])
        bmp += b'\x00' * padding
    return bytes(bmp)


def save_bmp(filename, bmp_data):
    with open(filename, 'wb') as f:
        f.write(bmp_data)


def solid_color(width, height, color):
    return [[color for _ in range(width)] for _ in range(height)]
# save_bmp("./output/solid_red.bmp", rgb_matrix_to_bmp(solid_color(400, 400, (255, 0, 0))))