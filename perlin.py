
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

# save_bmp("./output/perlin_noise.bmp", rgb_matrix_to_bmp(perlin_noise(
#     width=400,
#     height=400,
#     scale=50,
#     octaves=4,
#     persistence=0.5,
#     lacunarity=2.0,
#     seed=42
# )))



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

# save_bmp("./output/perlin_noise_color.bmp", rgb_matrix_to_bmp(perlin_noise_color(
#     width=400,
#     height=400,
#     scale=50,
#     octaves=4,
#     persistence=0.5,
#     lacunarity=2.0,
#     seed=42
# )))