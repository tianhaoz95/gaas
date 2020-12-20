import os

from gaas.applications.image_coloring.config import (
    ANIME_SKETCH_COLORIZATION_COLORGRAM_SCOPE,
    ANIME_SKETCH_COLORIZATION_DATA_SCOPE, ANIME_SKETCH_COLORIZATION_TRAIN_SCOPE,
    ANIME_SKETCH_COLORIZATION_VAL_SCOPE)


def get_data_location(dataset_root):
    return os.path.join(dataset_root, ANIME_SKETCH_COLORIZATION_DATA_SCOPE)


def get_colorgram_location(dataset_root):
    return os.path.join(get_data_location(dataset_root),
                        ANIME_SKETCH_COLORIZATION_COLORGRAM_SCOPE)


def get_train_location(dataset_root):
    return os.path.join(get_data_location(dataset_root),
                        ANIME_SKETCH_COLORIZATION_TRAIN_SCOPE)


def get_val_location(dataset_root):
    return os.path.join(get_data_location(dataset_root),
                        ANIME_SKETCH_COLORIZATION_VAL_SCOPE)
