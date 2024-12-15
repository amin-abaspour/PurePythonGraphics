

from bmp import rgb_matrix_to_bmp, save_bmp, solid_color

# --- Coordinate Mapping ---
def cartesian_to_screen(x, y, width, height):
    """Maps Cartesian coordinates to screen space (pixel coordinates)."""
    screen_x = int((x + 1) * width / 2)
    screen_y = int((1 - y) * height / 2)
    return screen_x, screen_y

def draw(pixel_matrix, shapes_points_colors):
    """Draw points on the given pixel matrix."""
    for points, color in shapes_points_colors:
        for x, y in points:
            pixel_matrix[y][x] = color
    return pixel_matrix


# --- Line Points Generator ---
def bresenham_line_points(x0, y0, x1, y1, width, height):
    """Generates the points of a line within grid bounds using Bresenham's algorithm."""
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        if 0 <= x0 < width and 0 <= y0 < height:
            points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    return points

# save_bmp("output/line.bmp", rgb_matrix_to_bmp(draw(
#     solid_color(400, 400, (255, 255, 255)),
#     bresenham_line_points(
#         *cartesian_to_screen(-0.5, 0.5, 400, 400),
#         *cartesian_to_screen(0.5, -0.5, 400, 400),
#         400, 400
#     ),
#     (0, 0, 0)
# )))

# save_bmp("output/line.bmp", rgb_matrix_to_bmp(draw(
#     solid_color(400, 400, (255, 255, 255)),
#     (
#       (
#         bresenham_line_points(*cartesian_to_screen(-0.5, 0.5, 400, 400), *cartesian_to_screen(0.5, -0.5, 400, 400), 400, 400),
#         (0, 0, 0)
#       ),
#     )
# )))

# x_line = bresenham_line_points(*cartesian_to_screen(-0.8,0,400,400), *cartesian_to_screen(0.8,0,400,400), 400,400)
# y_line = bresenham_line_points(*cartesian_to_screen(0,-0.8,400,400), *cartesian_to_screen(0,0.8,400,400), 400,400)
# x_end = cartesian_to_screen(0.8,0,400,400)
# y_end = cartesian_to_screen(0,0.8,400,400)
# x_arr1 = bresenham_line_points(x_end[0],x_end[1],x_end[0]-8,x_end[1]-8,400,400)
# x_arr2 = bresenham_line_points(x_end[0],x_end[1],x_end[0]-8,x_end[1]+8,400,400)
# y_arr1 = bresenham_line_points(y_end[0],y_end[1],y_end[0]-8,y_end[1]+8,400,400)
# y_arr2 = bresenham_line_points(y_end[0],y_end[1],y_end[0]+8,y_end[1]+8,400,400)
# save_bmp("output/axis.bmp", rgb_matrix_to_bmp(draw(
#     solid_color(400,400,(255,255,255)),
#     ((x_line,(0,0,0)),(y_line,(0,0,0)),(x_arr1,(0,0,0)),(x_arr2,(0,0,0)),(y_arr1,(0,0,0)),(y_arr2,(0,0,0)))
# )))



# --- General Conic ---
def conic(A, B, C, D, E, F, width, height, x_min, x_max, y_min, y_max):
    """Generates points for a general conic defined by Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0."""
    points = []
    for screen_y in range(height):
        for screen_x in range(width):
            # Map screen coordinates to Cartesian coordinates
            x = x_min + (screen_x / width) * (x_max - x_min)
            y = y_max - (screen_y / height) * (y_max - y_min)
            
            # Evaluate the conic equation in Cartesian space
            value = A * x**2 + B * x * y + C * y**2 + D * x + E * y + F
            threshold = (x_max - x_min) / width  # Adjust threshold dynamically
            if abs(value) < threshold:
                points.append((screen_x, screen_y))
    return points

# Circle: x^2 + y^2 - r^2 = 0
# save_bmp("output/circle.bmp", rgb_matrix_to_bmp(draw(
#     solid_color(400, 400, (255, 255, 255)),
#     (
#       (
#         conic(1, 0, 1, 0, 0, -1, 400, 400, -2, 2, -2, 2),
#         (255, 0, 0)
#       ),
#     )
# )))

# Ellipse: (x/a)^2 + (y/b)^2 - 1 = 0
# save_bmp("output/ellipse.bmp", rgb_matrix_to_bmp(draw(
#     solid_color(400, 400, (255, 255, 255)),
#     (
#       (
#         conic(1/0.8**2, 0, 1/0.5**2, 0, 0, -1, 400, 400, -1, 1, -1, 1),
#         (0, 255, 0)
#       ),
#     )
# )))

# Parabola: y^2 - 4px = 0
# save_bmp("output/parabola.bmp", rgb_matrix_to_bmp(draw(
#     solid_color(400, 400, (255, 255, 255)),
#     (
#       (
#         conic(0, 0, 1, -4*0.2, 0, 0, 400, 400, -1, 1, -1, 1),
#         (0, 0, 255)
#       ),
#     )
# )))

# Hyperbola: x^2/a^2 - y^2/b^2 - 1 = 0
# save_bmp("output/hyperbola.bmp", rgb_matrix_to_bmp(draw(
#     solid_color(400, 400, (255, 255, 255)),
#     (
#       (
#         conic(1/0.5**2, 0, -1/0.3**2, 0, 0, -1, 400, 400, -5, 5, -5, 5),
#         (0, 0, 0)
#       ),
#     )
# )))



from font import FONT, draw_char
# --- Drawing Axes with Labels ---
def draw_axes_with_labels():
    width, height = 400, 400
    # Create a white background
    pixel_matrix = solid_color(width, height, (255, 255, 255))
    
    # Generate axes lines
    x_line = bresenham_line_points(*cartesian_to_screen(-0.8, 0, width, height),
                                   *cartesian_to_screen(0.8, 0, width, height), width, height)
    y_line = bresenham_line_points(*cartesian_to_screen(0, -0.8, width, height),
                                   *cartesian_to_screen(0, 0.8, width, height), width, height)
    
    # Generate arrowheads for axes
    x_end = cartesian_to_screen(0.8, 0, width, height)
    y_end = cartesian_to_screen(0, 0.8, width, height)
    
    # Arrow for x-axis
    x_arrow1 = bresenham_line_points(x_end[0], x_end[1],
                                     x_end[0]-8, x_end[1]-8, width, height)
    x_arrow2 = bresenham_line_points(x_end[0], x_end[1],
                                     x_end[0]-8, x_end[1]+8, width, height)
    
    # Arrow for y-axis
    y_arrow1 = bresenham_line_points(y_end[0], y_end[1],
                                     y_end[0]-8, y_end[1]+8, width, height)
    y_arrow2 = bresenham_line_points(y_end[0], y_end[1],
                                     y_end[0]+8, y_end[1]+8, width, height)
    
    # Draw axes and arrowheads in black
    draw(pixel_matrix, (
        (x_line, (0, 0, 0)),
        (y_line, (0, 0, 0)),
        (x_arrow1, (0, 0, 0)),
        (x_arrow2, (0, 0, 0)),
        (y_arrow1, (0, 0, 0)),
        (y_arrow2, (0, 0, 0)),
    ))
    
    # Define label positions slightly offset from axis ends
    label_offset = 10  # pixels
    # For 'x' label
    x_label_pos = (x_end[0] + label_offset, x_end[1] - label_offset)
    # For 'y' label
    y_label_pos = (y_end[0] + label_offset, y_end[1] + label_offset)
    
    # Draw 'x' in red and 'y' in blue with scale 2 for better visibility
    draw_char(pixel_matrix, 'x', x_label_pos, (255, 0, 0), scale=2)
    draw_char(pixel_matrix, 'y', y_label_pos, (0, 0, 255), scale=2)
    
    # Save the image
    save_bmp("output/axis_with_labels.bmp", rgb_matrix_to_bmp(pixel_matrix))

# Call the function to draw axes with labels
draw_axes_with_labels()

