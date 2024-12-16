

from bmp import save_bmp, rgb_matrix_to_bmp, solid_color
from font import FONT


def get_char_bitmap(char):
    """Retrieve the bitmap for a given character, defaulting to space if not found."""
    return FONT.get(char.lower(), FONT[' '])

def draw_char(matrix, x, y, char, scale, fg, bg):
    """Draw a single character onto the matrix at position (x, y) with scaling."""
    bitmap = get_char_bitmap(char)
    for row_idx, row in enumerate(bitmap):
        for col_idx, pixel in enumerate(row):
            color = fg if pixel == '1' else bg
            for dy in range(scale):
                for dx in range(scale):
                    px, py = x + (col_idx * scale) + dx, y + (row_idx * scale) + dy
                    if 0 <= py < len(matrix) and 0 <= px < len(matrix[0]):
                        matrix[py][px] = color

def measure_text(text, scale=1, spacing=1):
    """Calculate the width and height of the rendered text."""
    char_width, char_height = 5, 5  # Based on FONT dimensions
    width = (char_width + spacing) * len(text) - spacing
    return width * scale, char_height * scale

def draw_text(matrix, text, scale, fg, bg):
    """Render text centered in the matrix."""
    text_w, text_h = measure_text(text, scale)
    img_h, img_w = len(matrix), len(matrix[0])
    start_x = (img_w - text_w) // 2
    start_y = (img_h - text_h) // 2
    spacing = scale
    char_scaled_width = 5 * scale

    for char in text:
        draw_char(matrix, start_x, start_y, char, scale, fg, bg)
        start_x += char_scaled_width + spacing

def create_text_image(width, height, text, fg=(0, 0, 0), bg=(255, 255, 255)):
    """Create an image matrix with the specified text, automatically scaling to fit."""
    # Calculate base dimensions
    base_char_width, base_char_height = 5, 5
    spacing = 1
    text_length = len(text)
    # Calculate maximum possible scale
    max_scale_width = width // ((base_char_width + spacing) * text_length - spacing)
    max_scale_height = height // base_char_height
    scale = min(max_scale_width, max_scale_height)
    scale = max(scale, 1)  # Ensure at least scale 1

    matrix = solid_color(width, height, bg)
    draw_text(matrix, text, scale, fg, bg)
    return matrix

# save_bmp("./output/abc.bmp", rgb_matrix_to_bmp(create_text_image(300, 100, "ABC")))
# save_bmp("./output/hello.bmp", rgb_matrix_to_bmp(create_text_image(300, 100, "Hello, World!")))
# save_bmp("./output/black.bmp", rgb_matrix_to_bmp(create_text_image(300, 100, "Black Mirror", fg=(255, 255, 255), bg=(0, 0, 0))))
# save_bmp("./output/point.bmp", rgb_matrix_to_bmp(create_text_image(300, 100, "What's the point of this, I'm so tired!", fg=(255, 0, 0), bg=(0, 255, 0))))
# save_bmp("./output/hate.bmp", rgb_matrix_to_bmp(create_text_image(300, 100, "I hate myself, I hate myself", fg=(0, 0, 255), bg=(255, 255, 0))))
