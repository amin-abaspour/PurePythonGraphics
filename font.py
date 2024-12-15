
# --- Simple Bitmap Font ---
FONT = {
    'x': [
        "10001",
        "01010",
        "00100",
        "01010",
        "10001",
    ],
    'y': [
        "10001",
        "01010",
        "00100",
        "00100",
        "00100",
    ],
    # Add more characters here if needed
}

def draw_char(pixel_matrix, char, position, color, scale=1):
    char = char.lower()
    if char not in FONT:
        print(f"Character '{char}' not in font.")
        return
    
    char_pattern = FONT[char]
    start_x, start_y = position
    
    for row_idx, row in enumerate(char_pattern):
        for col_idx, pixel in enumerate(row):
            if pixel == '1':
                for dy in range(scale):
                    for dx in range(scale):
                        x = start_x + col_idx * scale + dx
                        y = start_y + row_idx * scale + dy
                        if 0 <= y < len(pixel_matrix) and 0 <= x < len(pixel_matrix[0]):
                            pixel_matrix[y][x] = color
