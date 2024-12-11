

def overlay_patterns(base_pattern, overlay_pattern, width, height, blend_mode='override'):
    result_matrix = [row[:] for row in base_pattern]  # Copy base pattern

    for y in range(height):
        for x in range(width):
            base_color = base_pattern[y][x]
            overlay_color = overlay_pattern[y][x]

            if blend_mode == 'override':
                # Overlay color replaces base color unless overlay is black
                if overlay_color != (0, 0, 0):
                    result_matrix[y][x] = overlay_color
            elif blend_mode == 'add':
                # Additive blending (clamp to 255)
                result_matrix[y][x] = tuple(
                    min(base_color[i] + overlay_color[i], 255) for i in range(3)
                )
            elif blend_mode == 'multiply':
                # Multiply blending
                result_matrix[y][x] = tuple(
                    (base_color[i] * overlay_color[i]) // 255 for i in range(3)
                )
            else:
                raise ValueError("Unsupported blend mode")

    return result_matrix