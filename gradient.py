import math

def linear_gradient(width, height, start_color, end_color, angle=0):
    rgb_matrix = []
    angle_rad = math.radians(angle)
    for y in range(height):
        row = []
        for x in range(width):
            # Calculate gradient position along the angle
            ratio = ((x * math.cos(angle_rad)) + (y * math.sin(angle_rad))) / (width * math.cos(angle_rad) + height * math.sin(angle_rad))
            ratio = max(0, min(1, ratio))  # Clamp ratio to [0, 1]
            r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
            g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
            b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
            row.append((r, g, b))
        rgb_matrix.append(row)
    return rgb_matrix

# Example usage:
save_bmp(
    "./output/linear_gradient.bmp",  # Output file path
    rgb_matrix_to_bmp(
        linear_gradient(
            400,  # Width of the gradient
            400,  # Height of the gradient
            (0, 0, 255),  # Start color (Blue)
            (255, 0, 0),  # End color (Red)
            45  # Angle in degrees
        )
    )
)

def radial_gradient(width, height, center, radius, start_color, end_color):
    cx, cy = center
    rgb_matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            # Calculate distance from the center
            distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
            ratio = min(distance / radius, 1)  # Normalize and clamp to [0, 1]
            r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
            g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
            b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
            row.append((r, g, b))
        rgb_matrix.append(row)
    return rgb_matrix

# Example usage:
save_bmp(
    "./output/radial_gradient.bmp",  # Output file path
    rgb_matrix_to_bmp(
        radial_gradient(
            400,  # Width of the gradient
            400,  # Height of the gradient
            (200, 200),  # Center of the gradient (x, y)
            300,  # Radius of the gradient
            (255, 0, 0),  # Start color (Green)
            (0, 0, 255)  # End color (Blue)
        )
    )
)

def conic_gradient(width, height, center, color_stops):
    cx, cy = center
    rgb_matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            # Calculate angle relative to the center
            angle = math.atan2(y - cy, x - cx)  # Angle in radians
            normalized_angle = (angle + math.pi) / (2 * math.pi)  # Normalize to [0, 1]

            # Find the two closest color stops
            prev_stop, next_stop = None, None
            for stop in color_stops:
                if stop[0] <= normalized_angle:
                    prev_stop = stop
                if stop[0] > normalized_angle and next_stop is None:
                    next_stop = stop
                    break

            # Handle boundary cases
            if prev_stop is None:
                prev_stop = color_stops[-1]
            if next_stop is None:
                next_stop = color_stops[0]

            # Interpolate colors between the two stops
            segment_ratio = (normalized_angle - prev_stop[0]) / (next_stop[0] - prev_stop[0]) if next_stop[0] != prev_stop[0] else 0
            r = int(prev_stop[1][0] + (next_stop[1][0] - prev_stop[1][0]) * segment_ratio)
            g = int(prev_stop[1][1] + (next_stop[1][1] - prev_stop[1][1]) * segment_ratio)
            b = int(prev_stop[1][2] + (next_stop[1][2] - prev_stop[1][2]) * segment_ratio)

            row.append((r, g, b))
        rgb_matrix.append(row)
    return rgb_matrix

# Example usage:
save_bmp(
    "./output/conic_gradient.bmp",  # Output file path
    rgb_matrix_to_bmp(
        conic_gradient(
            400,  # Width of the gradient
            400,  # Height of the gradient
            (200, 200),  # Center of the gradient (x, y)
            [
                (0.0, (255, 0, 0)),  # Red color at angle 0.0 (normalized)
                (0.50, (0, 0, 255)),  # Blue color at angle 0.5 (normalized)
                (1.0, (255, 0, 0)) # Blue color at angle 1.0 (normalized)
            ]
        )
    )
)

def angular_gradient(width, height, center, start_color, end_color):
    # Angular gradient is a special case of conic gradient with only two color stops
    return conic_gradient(
        width,  # Width of the gradient
        height,  # Height of the gradient
        center,  # Center of the gradient (x, y)
        [
            (0.0, start_color),  # Start color at angle 0.0 (normalized)
            (0.50, end_color),  # End color at angle 1.0 (normalized)
            (1.0, start_color)  # End color at angle 1.0 (normalized)
        ]
    )

# Example usage:
save_bmp(
    "./output/angular_gradient.bmp",  # Output file path
    rgb_matrix_to_bmp(
        angular_gradient(
            400,  # Width of the gradient
            400,  # Height of the gradient
            (200, 200),  # Center of the gradient (x, y)
            (255, 0, 0),  # Start color (Red)
            (0, 0, 255)  # End color (Blue)
        )
    )
)