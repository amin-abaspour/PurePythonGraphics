
import math
import random

def validate_rgb_matrix(rgb_matrix):
    """Ensure that the RGB matrix is properly structured."""
    height = len(rgb_matrix)
    if height == 0:
        raise ValueError("RGB matrix has no rows.")
    
    width = len(rgb_matrix[0])
    for row in rgb_matrix:
        if len(row) != width:
            raise ValueError("All rows in the RGB matrix must have the same length.")
        for pixel in row:
            if not isinstance(pixel, tuple) or len(pixel) != 3:
                raise ValueError(f"Invalid pixel value {pixel}. Each pixel must be a tuple of 3 integers.")
            if not all(0 <= value <= 255 for value in pixel):
                raise ValueError(f"Pixel value out of range: {pixel}. RGB values must be in the range 0-255.")

def rgb_matrix_to_ppm(rgb_matrix, max_color=255):
  height, width = len(rgb_matrix), len(rgb_matrix[0])
  ppm = ["P3", f"{width} {height}", f"{max_color}"]
  # Iterates over each row and converts each pixel tuple (R, G, B) into space-separated strings.
  for row in rgb_matrix:
    # Flatten the row of tuples into a list of integers
    pixel_values = ' '.join(f"{r} {g} {b}" for r, g, b in row)
    ppm.append(pixel_values)
  ppm_string = '\n'.join(ppm) + '\n'
  return ppm_string


def rgb_matrix_to_bmp(rgb_matrix):
    validate_rgb_matrix(rgb_matrix)  # Validate the input
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

