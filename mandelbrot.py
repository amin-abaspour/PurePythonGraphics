
def mandelbrot_set(width, height, max_iterations=100, x_min=-2.0, x_max=1.0, y_min=-1.5, y_max=1.5, color_map=None):
    if color_map is None:
        def color_map(iteration):
            return (0, 0, 0) if iteration == max_iterations else (255 - int(iteration * 255 / max_iterations),) * 3
    rgb_matrix = []
    for y in range(height):
        cy = y_min + (y / height) * (y_max - y_min)
        row = []
        for x in range(width):
            cx = x_min + (x / width) * (x_max - x_min)
            c, z, iteration = complex(cx, cy), 0, 0
            while abs(z) <= 2 and iteration < max_iterations:
                z = z * z + c
                iteration += 1
            row.append(color_map(iteration))
        rgb_matrix.append(row)
    return rgb_matrix

def rainbow_color_map(iteration, max_iterations=100):
    if iteration == max_iterations:
        return (0, 0, 0)
    t = iteration / max_iterations
    r = int(9*(1-t)*t*t*t*255)
    g = int(15*(1-t)**2*t*t*255)
    b = int(8.5*(1-t)**3*t*255)
    return (r, g, b)

# Example Usage
mandelbrot = mandelbrot_set(
    width=800,
    height=600,
    max_iterations=100,
    x_min=-2.5,
    x_max=1.5,
    y_min=-1.5,
    y_max=1.5
)
# save_bmp("./output/mandelbrot_grayscale.bmp", rgb_matrix_to_bmp(mandelbrot))

mandelbrot_rainbow = mandelbrot_set(
    width=800,
    height=600,
    max_iterations=100,
    x_min=-2.5,
    x_max=1.5,
    y_min=-1.5,
    y_max=1.5,
    color_map=lambda iter: rainbow_color_map(iter, max_iterations=100)
)
# save_bmp("./output/mandelbrot_rainbow.bmp", rgb_matrix_to_bmp(mandelbrot_rainbow))