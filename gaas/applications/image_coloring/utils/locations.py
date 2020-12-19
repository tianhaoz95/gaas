import os

from gaas.applications.image_coloring.config import \
    ANIME_SKETCH_COLORIZATION_COLORGRAM_SCOPE


def get_colorgram_location(dataset_root):
    return os.path.join(dataset_root, 'data',
                        ANIME_SKETCH_COLORIZATION_COLORGRAM_SCOPE)
