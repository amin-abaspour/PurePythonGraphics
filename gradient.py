import math
from image import rgb_matrix_to_bmp, save_bmp

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

def interpolate_color(c1, c2, t):
    """
    Linearly interpolate between two RGB colors c1 and c2, with t in [0,1].
    c1, c2 are (r,g,b) tuples.
    """
    r = int(c1[0] + (c2[0] - c1[0]) * t)
    g = int(c1[1] + (c2[1] - c1[1]) * t)
    b = int(c1[2] + (c2[2] - c1[2]) * t)
    return (r, g, b)

def find_color_for_angle(angle, color_stops):
    """
    Given an angle in degrees [0,360), return the interpolated color from the color_stops.
    color_stops: a list of (angle, (r,g,b)) where angle is in [0,360].
    """
    # Normalize angle to [0,360)
    angle = angle % 360
    
    for i in range(len(color_stops) - 1):
        a1, c1 = color_stops[i]
        a2, c2 = color_stops[i+1]
        if a1 <= angle < a2:
            t = (angle - a1) / (a2 - a1)
            return interpolate_color(c1, c2, t)
    
    # If we somehow don't find a segment (shouldn't happen), return last color
    return color_stops[-1][1]

def conic_gradient(width, height, center, color_stops, angle_offset=0):
    """
    Generate a conic gradient as a matrix [height][width][(r,g,b)].

    Parameters:
    - width, height: dimensions of the image.
    - center: (cx, cy) the center of the gradient.
    - color_stops: list of (angle, (r,g,b)) tuples. Angles can be any range,
      e.g. [(90, (255,0,0)), (450, (0,0,255))].
    - angle_offset: rotate the entire gradient by this angle in degrees.

    Returns:
    A nested list (height x width) of (r,g,b) tuples.
    """

    # Sort stops by angle
    color_stops = sorted(color_stops, key=lambda x: x[0])
    
    # Normalize angles so that the first stop starts at 0°
    base_angle = color_stops[0][0]
    normalized_stops = []
    for (a, c) in color_stops:
        normalized_stops.append((a - base_angle, c))
    
    # Adjust angle_offset so the visual orientation remains as intended
    angle_offset = (angle_offset + base_angle) % 360
    
    # After normalization, first stop is at 0°. Let's ensure we have a full 360° coverage:
    # Find the last stop angle
    last_angle = normalized_stops[-1][0]
    if last_angle < 360:
        # Append a wrap-around stop at 360°, same color as the first stop to close the loop
        normalized_stops.append((360, normalized_stops[0][1]))
    elif last_angle > 360:
        # If last angle exceeds 360, we can still use modulo logic.
        # For simplicity, if last_angle == 360 exactly or slightly more, we can clamp it.
        # Ideally, user should define a full 360 cycle. We trust it's 360 for a closed loop.
        pass
    else:
        # If last_angle == 360 exactly, perfect, we already have a full loop.
        pass

    # Construct image
    cx, cy = center
    image = []
    for y in range(height):
        row = []
        for x in range(width):
            dx = x - cx
            dy = y - cy
            # Compute angle in degrees
            angle = math.degrees(math.atan2(dy, dx))
            if angle < 0:
                angle += 360
            # Apply angle offset
            angle = (angle + angle_offset) % 360
            
            # Get color for this angle
            color = find_color_for_angle(angle, normalized_stops)
            row.append(color)
        image.append(row)
    return image


def angular_gradient(width, height, center, start_color, end_color):
    # Angular gradient is a special case of a conic gradient with only two color stops.
    # Here, we define three stops at 0°, 180°, and 360° to create a half-circle transition
    # from start_color to end_color, and then back to start_color.
    return conic_gradient(
        width,
        height,
        center,
        [
            (0,   start_color),  # Start color at 0°
            (180, end_color),    # End color at 180°
            (360, start_color)   # Back to start color at 360°
        ]
    )

