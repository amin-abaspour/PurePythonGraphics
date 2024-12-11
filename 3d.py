
from image import rgb_matrix_to_bmp, save_bmp
import math

def generate_shaded_sphere(width, height, sphere_center, sphere_radius, light_dir, sphere_color, background_color):
    rgb_matrix = [[background_color for _ in range(width)] for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            # Convert pixel coordinate to Cartesian coordinates with origin at sphere_center
            dx = x - sphere_center[0]
            dy = y - sphere_center[1]
            distance_sq = dx * dx + dy * dy

            if distance_sq <= sphere_radius * sphere_radius:
                # Calculate z coordinate on the sphere's surface
                z = math.sqrt(sphere_radius * sphere_radius - distance_sq)
                
                # Surface normal (x, y, z) normalized
                nx = dx / sphere_radius
                ny = dy / sphere_radius
                nz = z / sphere_radius
                
                # Dot product with light direction
                dot = nx * light_dir[0] + ny * light_dir[1] + nz * light_dir[2]
                dot = max(dot, 0)  # Clamp to [0, 1]
                
                # Simple shading: scale color by dot product
                shaded_color = (
                    int(sphere_color[0] * dot),
                    int(sphere_color[1] * dot),
                    int(sphere_color[2] * dot)
                )
                
                rgb_matrix[y][x] = shaded_color

    return rgb_matrix

def normalize_vector(v):
    length = math.sqrt(sum([coord ** 2 for coord in v]))
    return tuple(coord / length for coord in v)

# Image dimensions
WIDTH = 400
HEIGHT = 400

# Sphere parameters
sphere_center = (WIDTH // 2, HEIGHT // 2)
sphere_radius = min(WIDTH, HEIGHT) // 3
sphere_color = (70, 130, 180)  # Steel Blue
background_color = (0, 0, 0)  # Dark Gray

# Light direction (normalized)
light_dir = normalize_vector((1, 1, 1))  # Light coming from top-right-front

# Generate the shaded sphere
rgb_matrix = generate_shaded_sphere(
    width=WIDTH,
    height=HEIGHT,
    sphere_center=sphere_center,
    sphere_radius=sphere_radius,
    light_dir=light_dir,
    sphere_color=sphere_color,
    background_color=background_color
)

# Save the image
bmp_data = rgb_matrix_to_bmp(rgb_matrix)
save_bmp("./output/shaded_sphere.bmp", bmp_data)
