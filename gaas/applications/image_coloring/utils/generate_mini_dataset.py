import os
import pathlib
import shutil
from typing import List

from gaas.applications.image_coloring.config import \
    ANIME_SKETCH_COLORIZATION_DATASET_DATASET_ID
from gaas.applications.image_coloring.dataset import \
    AnimeSketchColorizationDatasetGenerator
from gaas.applications.image_coloring.utils.locations import (
    get_colorgram_location, get_train_location, get_val_location)
from gaas.config import global_logger
from gaas.utils.exec_mode import get_data_root
from gaas.utils.filesys import create_dir_if_not_exist, recreate_dir
from gaas.utils.kaggle import get_extract_location


def get_data_ids(location) -> List[str]:
    root = pathlib.Path(location)
    files = root.glob('*')
    data_ids = []
    for file in files:
        data_id = file.parts[-1].split('.')[0]
        data_ids.append(data_id)
    return data_ids


def generate_mini_dataset() -> None:
    _ = AnimeSketchColorizationDatasetGenerator(type='PROD')
    dev_dataset_root = get_data_root('DEV')
    prod_dataset_root = get_data_root('PROD')
    dev_dataset_location = get_extract_location(
        dev_dataset_root, ANIME_SKETCH_COLORIZATION_DATASET_DATASET_ID)
    prod_dataset_location = get_extract_location(
        prod_dataset_root, ANIME_SKETCH_COLORIZATION_DATASET_DATASET_ID)
    recreate_dir(dev_dataset_location)
    dev_colorgram_location = get_colorgram_location(dev_dataset_location)
    dev_train_location = get_train_location(dev_dataset_location)
    dev_val_location = get_val_location(dev_dataset_location)
    prod_colorgram_location = get_colorgram_location(prod_dataset_location)
    prod_train_location = get_train_location(prod_dataset_location)
    prod_val_location = get_val_location(prod_dataset_location)
    create_dir_if_not_exist(dev_colorgram_location)
    create_dir_if_not_exist(dev_train_location)
    create_dir_if_not_exist(dev_val_location)
    train_ids = get_data_ids(prod_train_location)[:10]
    val_ids = get_data_ids(prod_val_location)[:10]
    colorgram_ids = get_data_ids(prod_colorgram_location)[:10]
    for train_id in train_ids:
        shutil.copyfile(
            os.path.join(prod_train_location, '{id}.png'.format(id=train_id)),
            os.path.join(dev_train_location, '{id}.png'.format(id=train_id)))
    for val_id in val_ids:
        shutil.copyfile(
            os.path.join(prod_val_location, '{id}.png'.format(id=val_id)),
            os.path.join(dev_val_location, '{id}.png'.format(id=val_id)))
    for colorgram_id in colorgram_ids:
        shutil.copyfile(
            os.path.join(prod_colorgram_location,
                         '{id}.json'.format(id=colorgram_id)),
            os.path.join(dev_colorgram_location,
                         '{id}.json'.format(id=colorgram_id)))
    global_logger.info('Generate mini dataset done.')
