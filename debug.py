


def validate_pixel_matrix(pixel_matrix, pixel_format='RGB'):

    supported_formats = {
        'RGB': (3, [(0, 255), (0, 255), (0, 255)]),
        'RGBA': (4, [(0, 255), (0, 255), (0, 255), (0, 255)]),
        'Grayscale': (1, [(0, 255)]),
        'CMYK': (4, [(0, 255), (0, 255), (0, 255), (0, 255)]),
        'HSB': (3, [(0, 360), (0, 100), (0, 100)]),
        'HSV': (3, [(0, 360), (0, 100), (0, 100)]),
    }

    if pixel_format not in supported_formats:
        raise ValueError(f"Unsupported pixel format: {pixel_format}. Supported formats: {list(supported_formats.keys())}")
    
    expected_length, component_ranges = supported_formats[pixel_format]

    # Validate the matrix structure
    if not isinstance(pixel_matrix, list) or not all(isinstance(row, list) for row in pixel_matrix):
        raise ValueError("Pixel matrix must be a list of lists.")

    if not pixel_matrix or not pixel_matrix[0]:  # Check for empty matrix or empty rows
        raise ValueError("Pixel matrix must not be empty and must contain non-empty rows.")
    
    # Check if all rows have the same length
    first_row_length = len(pixel_matrix[0])
    if any(len(row) != first_row_length for row in pixel_matrix):
        raise ValueError(
            f"Row length inconsistency: all rows must have the same length of {first_row_length}."
        )

    # Validate each pixel in the matrix
    for row_idx, row in enumerate(pixel_matrix):
        for col_idx, pixel in enumerate(row):
            # Ensure pixel is a tuple with the correct number of components
            if not isinstance(pixel, tuple) or len(pixel) != expected_length:
                raise ValueError(
                    f"Invalid pixel at row {row_idx}, column {col_idx}: {pixel}. "
                    f"Expected a tuple of {expected_length} values for {pixel_format}."
                )
            # Validate each component against the corresponding range
            for component, (min_val, max_val) in zip(pixel, component_ranges):
                if not isinstance(component, int) or not (min_val <= component <= max_val):
                    raise ValueError(
                        f"Pixel value out of range at row {row_idx}, column {col_idx}: {pixel}. "
                        f"Expected values in ranges {component_ranges} for {pixel_format}."
                    )



def debug_pixel_matrix(pixel_matrix):

    if not isinstance(pixel_matrix, list):
        return {"error": "Pixel matrix is not a list of lists."}

    debug_info = {
        "total_rows": len(pixel_matrix),
        "row_lengths": [],
        "max_row_length": 0,
        "min_row_length": float('inf'),
        "invalid_pixels": [],
        "summary": "",
    }

    for row_idx, row in enumerate(pixel_matrix):
        if not isinstance(row, list):
            debug_info["summary"] = f"Row {row_idx} is not a list."
            return debug_info
        
        row_length = len(row)
        debug_info["row_lengths"].append(row_length)
        debug_info["max_row_length"] = max(debug_info["max_row_length"], row_length)
        debug_info["min_row_length"] = min(debug_info["min_row_length"], row_length)

        for col_idx, pixel in enumerate(row):
            if not isinstance(pixel, tuple) or len(pixel) not in {1, 3, 4}:
                debug_info["invalid_pixels"].append(
                    {"row": row_idx, "col": col_idx, "value": pixel, "reason": "Invalid format"}
                )
            elif any(not isinstance(value, int) or not (0 <= value <= 255) for value in pixel):
                debug_info["invalid_pixels"].append(
                    {"row": row_idx, "col": col_idx, "value": pixel, "reason": "Out-of-range values"}
                )

    if not debug_info["row_lengths"]:
        debug_info["summary"] = "The pixel matrix is empty."
    elif len(set(debug_info["row_lengths"])) > 1:
        debug_info["summary"] = "Row lengths are inconsistent."
    elif debug_info["invalid_pixels"]:
        debug_info["summary"] = f"Detected {len(debug_info['invalid_pixels'])} invalid pixels."
    else:
        debug_info["summary"] = "The pixel matrix is valid."

    return debug_info
