import pathlib

from gaas.applications.image_coloring.config import \
    ANIME_SKETCH_COLORIZATION_DATASET_DATASET_ID
from gaas.applications.image_coloring.dataset import \
    AnimeSketchColorizationDatasetGenerator
from gaas.applications.image_coloring.utils.locations import \
    get_colorgram_location
from gaas.config import global_logger
from gaas.utils.exec_mode import get_data_root
from gaas.utils.filesys import recreate_dir
from gaas.utils.kaggle import get_extract_location


def generate_mini_dataset() -> None:
    _ = AnimeSketchColorizationDatasetGenerator(type='PROD')
    dev_dataset_root = get_data_root('DEV')
    prod_dataset_root = get_data_root('PROD')
    dev_dataset_location = get_extract_location(
        dev_dataset_root, ANIME_SKETCH_COLORIZATION_DATASET_DATASET_ID)
    prod_dataset_location = get_extract_location(
        prod_dataset_root, ANIME_SKETCH_COLORIZATION_DATASET_DATASET_ID)
    recreate_dir(dev_dataset_location)
    global_logger.info(get_colorgram_location(prod_dataset_location))
    colorgram_root = pathlib.Path(get_colorgram_location(prod_dataset_location))
    colorgram_files = colorgram_root.glob('*')
    # TODO: finish impl for the mini dataset generation.
    """
    1) Convert the color gram files to ids.
    2) Randomly select a subset of ids.
    3) Move the corresponding files to the mini set.
    4) Zip the files to mimic the downloading process.
    """
    data_ids = []
    for colorgram_file in colorgram_files:
        data_id = colorgram_file.split('.')[0]
        data_ids.append(data_id)
    subset_ids = data_ids[:10]
    for subset_id in subset_ids:
        # Copy colorgram
        pass
