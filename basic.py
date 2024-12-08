

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

def rgb_matrix(width, height, color):
    return [[color for _ in range(width)] for _ in range(height)]


def horizontal_gradient(width, height, start_color, end_color):
    rgb_matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            ratio = x / (width - 1)
            r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
            g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
            b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
            row.append((r, g, b))
        rgb_matrix.append(row)
    return rgb_matrix

def checkerboard(width, height, square_size, color1, color2):
    rgb_matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            if ((x // square_size) + (y // square_size)) % 2 == 0:
                row.append(color1)
            else:
                row.append(color2)
        rgb_matrix.append(row)
    return rgb_matrix

def horizontal_stripes(width, height, stripe_height, color1, color2):
    rgb_matrix = []
    for y in range(height):
        row = []
        current_color = color1 if (y // stripe_height) % 2 == 0 else color2
        for x in range(width):
            row.append(current_color)
        rgb_matrix.append(row)
    return rgb_matrix

# save_bmp("solid_red.bmp", rgb_matrix_to_bmp(rgb_matrix(400, 400, (255, 0, 0))))
# save_bmp("horizontal_gradient.bmp", rgb_matrix_to_bmp(horizontal_gradient(400, 400, (0, 0, 255), (255, 0, 0))))
# save_bmp("checkerboard.bmp", rgb_matrix_to_bmp(checkerboard(400, 400, 40, (255, 255, 255), (0, 0, 0))))
# save_bmp("horizontal_stripes.bmp", rgb_matrix_to_bmp(horizontal_stripes(400, 400, 40, (255, 0, 0), (0, 0, 255))))

import math
def circular_gradient(width, height, center, inner_color, outer_color, radius):
    cx, cy = center
    def interpolate_color(distance):
        ratio = min(distance / radius, 1.0)
        return tuple(int(inner_color[i] + (outer_color[i] - inner_color[i]) * ratio) for i in range(3))
    def pixel_color(x, y):
        distance = math.sqrt((x - cx)**2 + (y - cy)**2)
        return interpolate_color(distance)
    return [[pixel_color(x, y) for x in range(width)] for y in range(height)]

# save_bmp("circular_gradient.bmp", rgb_matrix_to_bmp(circular_gradient(400, 400, (200, 200), (255, 255, 255), (0, 0, 0), 200)))


import math
import random

def perlin_noise(width, height, scale=50, octaves=4, persistence=0.5, lacunarity=2.0, seed=None):
    if seed is not None:
        random.seed(seed)
    def lerp(a, b, t):
        return a + t * (b - a)
    def fade(t):
        return t * t * t * (t * (t * 6 - 15) + 10)
    def grad(hash, x, y):
        h = hash & 3
        u = x if h < 2 else y
        v = y if h < 2 else x
        return (u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v)
    permutation = list(range(256))
    random.shuffle(permutation)
    permutation += permutation
    def perlin(x, y):
        xi = int(math.floor(x)) & 255
        yi = int(math.floor(y)) & 255
        xf = x - math.floor(x)
        yf = y - math.floor(y)
        u = fade(xf)
        v = fade(yf)
        aa = permutation[permutation[xi] + yi]
        ab = permutation[permutation[xi] + yi + 1]
        ba = permutation[permutation[xi + 1] + yi]
        bb = permutation[permutation[xi + 1] + yi + 1]
        x1 = lerp(grad(aa, xf, yf), grad(ba, xf - 1, yf), u)
        x2 = lerp(grad(ab, xf, yf - 1), grad(bb, xf - 1, yf - 1), u)
        return lerp(x1, x2, v)
    noise = [[0 for _ in range(width)] for _ in range(height)]
    max_amp = 0
    amplitude = 1
    frequency = 1
    for _ in range(octaves):
        for y in range(height):
            for x in range(width):
                noise[y][x] += perlin(x / scale * frequency, y / scale * frequency) * amplitude
        max_amp += amplitude
        amplitude *= persistence
        frequency *= lacunarity
    rgb_matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            value = int((noise[y][x] / max_amp + 1) / 2 * 255)
            value = max(0, min(255, value))
            row.append((value, value, value))
        rgb_matrix.append(row)
    return rgb_matrix

save_bmp("perlin_noise.bmp", rgb_matrix_to_bmp(perlin_noise(
    width=400,
    height=400,
    scale=50,
    octaves=4,
    persistence=0.5,
    lacunarity=2.0,
    seed=42
)))



def perlin_noise_color(width, height, scale=50, octaves=4, persistence=0.5, lacunarity=2.0, seed=None):
    if seed is not None:
        random.seed(seed)
    
    def lerp(a, b, t):
        return a + t * (b - a)
    
    def fade(t):
        return t * t * t * (t * (t * 6 - 15) + 10)
    
    def grad(hash, x, y):
        h = hash & 3
        u = x if h < 2 else y
        v = y if h < 2 else x
        return (u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v)
    
    permutation = list(range(256))
    random.shuffle(permutation)
    permutation += permutation
    
    def perlin(x, y):
        xi = int(math.floor(x)) & 255
        yi = int(math.floor(y)) & 255
        xf = x - math.floor(x)
        yf = y - math.floor(y)
        
        u = fade(xf)
        v = fade(yf)
        
        aa = permutation[permutation[xi] + yi]
        ab = permutation[permutation[xi] + yi + 1]
        ba = permutation[permutation[xi + 1] + yi]
        bb = permutation[permutation[xi + 1] + yi + 1]
        
        x1 = lerp(grad(aa, xf, yf), grad(ba, xf - 1, yf), u)
        x2 = lerp(grad(ab, xf, yf - 1), grad(bb, xf - 1, yf - 1), u)
        return lerp(x1, x2, v)
    
    noise_r = [[0 for _ in range(width)] for _ in range(height)]
    noise_g = [[0 for _ in range(width)] for _ in range(height)]
    noise_b = [[0 for _ in range(width)] for _ in range(height)]
    max_amp = 0
    amplitude = 1
    frequency = 1
    
    for _ in range(octaves):
        for y in range(height):
            for x in range(width):
                noise_r[y][x] += perlin(x / scale * frequency, y / scale * frequency) * amplitude
                noise_g[y][x] += perlin((x + 100) / scale * frequency, (y + 100) / scale * frequency) * amplitude
                noise_b[y][x] += perlin((x + 200) / scale * frequency, (y + 200) / scale * frequency) * amplitude
        max_amp += amplitude
        amplitude *= persistence
        frequency *= lacunarity
    
    rgb_matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            r = int((noise_r[y][x] / max_amp + 1) / 2 * 255)
            g = int((noise_g[y][x] / max_amp + 1) / 2 * 255)
            b = int((noise_b[y][x] / max_amp + 1) / 2 * 255)
            row.append((max(0, min(255, r)),
                        max(0, min(255, g)),
                        max(0, min(255, b))))
        rgb_matrix.append(row)
    
    return rgb_matrix

# Example Usage: Save Colored Perlin Noise Image
save_bmp("perlin_noise_color.bmp", rgb_matrix_to_bmp(perlin_noise_color(
    width=400,
    height=400,
    scale=50,
    octaves=4,
    persistence=0.5,
    lacunarity=2.0,
    seed=42
)))
