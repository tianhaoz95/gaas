import numpy as np


def normalize_image(raw_pixels: np.array) -> np.array:
    mean_pixel_val = 127.5
    normalized_image = (raw_pixels - mean_pixel_val) / mean_pixel_val
    return normalized_image
