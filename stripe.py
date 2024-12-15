
from bmp import rgb_matrix_to_bmp, save_bmp
from mathematics import degree_to_radian, sine, cosine

import math

def cartesian_stripes(width, height, stripe_size, color1, color2, angle=0):
    rgb_matrix = []
    angle_rad = degree_to_radian(angle)  # Convert angle to radians
    for y in range(height):
        row = []
        for x in range(width):
            # Calculate the distance along the direction of the angle
            stripe_index = int((x * cosine(angle_rad) + y * sine(angle_rad)) / stripe_size)
            current_color = color1 if stripe_index % 2 == 0 else color2
            row.append(current_color)
        rgb_matrix.append(row)
    return rgb_matrix

# save_bmp("./output/horizontal_stripes.bmp", rgb_matrix_to_bmp(cartesian_stripes(400, 400, 20, (255, 165, 0), (0, 128, 255), 0)))
# save_bmp("./output/diagonal_stripes.bmp", rgb_matrix_to_bmp(cartesian_stripes(400, 400, 30, (255, 255, 0), (128, 0, 128), 45)))
# save_bmp("./output/vertical_stripes.bmp", rgb_matrix_to_bmp(cartesian_stripes(400, 400, 15, (0, 255, 0), (0, 0, 128), 90)))
# save_bmp("./output/arbitrary_stripes.bmp", rgb_matrix_to_bmp(cartesian_stripes(400, 400, 25, (255, 105, 180), (75, 0, 130), 25)))

def radial_stripes(width, height, stripe_size, color1, color2, center=None):
    if center is None:
        center = (width // 2, height // 2)  # Default to the center of the image
    cx, cy = center
    rgb_matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            # Calculate distance from the center
            distance = int(((x - cx) ** 2 + (y - cy) ** 2) ** 0.5)
            stripe_index = distance // stripe_size
            current_color = color1 if stripe_index % 2 == 0 else color2
            row.append(current_color)
        rgb_matrix.append(row)
    return rgb_matrix

# save_bmp("./output/radial_stripes_center.bmp", rgb_matrix_to_bmp(radial_stripes(400, 400, 20, (255, 255, 255), (0, 0, 0))))
# save_bmp("./output/radial_stripes_left.bmp", rgb_matrix_to_bmp(radial_stripes(400, 400, 20, (255, 255, 255), (0, 0, 0), (0, 200))))
# save_bmp("./output/radial_stripes_topright.bmp", rgb_matrix_to_bmp(radial_stripes(400, 400, 20, (255, 255, 255), (0, 0, 0), (400, 0))))

def wavy_stripes(width, height, stripe_size, color1, color2, frequency=1.0, amplitude=10):
    import math
    rgb_matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            wave_offset = int(amplitude * math.sin(2 * math.pi * frequency * y / height))
            stripe_index = ((x + wave_offset) // stripe_size) % 2
            current_color = color1 if stripe_index == 0 else color2
            row.append(current_color)
        rgb_matrix.append(row)
    return rgb_matrix
# save_bmp("./output/wavy_stripes.bmp", rgb_matrix_to_bmp(wavy_stripes(400, 400, 20, (0, 255, 0), (0, 0, 0), 3, 20)))

def wavy_radial_stripes(width, height, stripe_size, color1, color2, frequency=1.0, amplitude=10, center=None):
    if center is None:
        center = (width // 2, height // 2)
    cx, cy = center
    rgb_matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            dx, dy = x - cx, y - cy
            distance = ((dx ** 2 + dy ** 2) ** 0.5)
            wave_offset = amplitude * math.sin(2 * math.pi * frequency * math.atan2(dy, dx))
            effective_distance = distance + wave_offset
            stripe_index = int(effective_distance // stripe_size)
            current_color = color1 if stripe_index % 2 == 0 else color2
            row.append(current_color)
        rgb_matrix.append(row)
    return rgb_matrix
# save_bmp("./output/wavy_radial_stripes.bmp", rgb_matrix_to_bmp(wavy_radial_stripes(400, 400, 20, (0, 128, 255), (255, 165, 0), 3, 15)))

def concentric_gradient_stripes(width, height, stripe_size, colors, center=None):
    if center is None:
        center = (width // 2, height // 2)
    cx, cy = center
    rgb_matrix = []
    num_colors = len(colors)
    for y in range(height):
        row = []
        for x in range(width):
            distance = int(((x - cx) ** 2 + (y - cy) ** 2) ** 0.5)
            stripe_index = (distance // stripe_size) % num_colors
            current_color = colors[stripe_index]
            row.append(current_color)
        rgb_matrix.append(row)
    return rgb_matrix
# save_bmp("./output/concentric_gradient_stripes.bmp", rgb_matrix_to_bmp(concentric_gradient_stripes(400, 400, 20, [(255, 0, 0), (0, 255, 0), (0, 0, 255)])))

def starburst_pattern(width, height, stripe_size, color1, color2, center=None):
    if center is None:
        center = (width // 2, height // 2)
    cx, cy = center
    rgb_matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            angle = int((math.atan2(y - cy, x - cx) + math.pi) / (2 * math.pi) * stripe_size)
            stripe_index = angle % 2
            current_color = color1 if stripe_index == 0 else color2
            row.append(current_color)
        rgb_matrix.append(row)
    return rgb_matrix
# save_bmp("./output/starburst_pattern.bmp", rgb_matrix_to_bmp(starburst_pattern(8000, 8000, 20, (255, 255, 0), (0, 0, 0))))

def hexagonal_grid(width, height, cell_size, color1, color2):
    rgb_matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            hex_x = x // (cell_size * 3 // 4)
            hex_y = (y - (hex_x % 2) * (cell_size // 2)) // cell_size
            cell_index = (hex_x + hex_y) % 2
            current_color = color1 if cell_index == 0 else color2
            row.append(current_color)
        rgb_matrix.append(row)
    return rgb_matrix
# save_bmp("./output/hexagonal_grid.bmp", rgb_matrix_to_bmp(hexagonal_grid(400, 400, 30, (128, 0, 128), (255, 255, 255))))

def checkerboard(width, height, cell_size, color1, color2):
    rgb_matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            # Alternate colors based on the sum of x and y indices divided by cell size
            cell_index = ((x // cell_size) + (y // cell_size)) % 2
            current_color = color1 if cell_index == 0 else color2
            row.append(current_color)
        rgb_matrix.append(row)
    return rgb_matrix
# save_bmp("./output/checkerboard.bmp", rgb_matrix_to_bmp(checkerboard(400, 400, 20, (255, 255, 255), (0, 0, 0))))
