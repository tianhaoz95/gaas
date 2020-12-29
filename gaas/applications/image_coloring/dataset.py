import logging
import os
import zipfile
from pathlib import Path
from subprocess import PIPE, Popen

import tensorflow as tf
from gaas.applications.image_coloring.config import (
    ANIME_SKETCH_COLORIZATION_DATASET_DATASET_ID,
    ANIME_SKETCH_COLORIZATION_DATASET_KAGGLE_ID)
from gaas.utils.exec_mode import get_data_root
from gaas.utils.filesys import create_dir_if_not_exist
from gaas.utils.github import get_kaggle_credential
from gaas.utils.kaggle import (get_extract_location, get_kaggle_dataset_id,
                               get_zipfile_location,
                               maybe_extract_kaggle_dataset,
                               maybe_fetch_kaggle_dataset)
from gaas.utils.normalization import normalize_image
from tensorflow.keras.preprocessing.image import img_to_array, load_img


class AnimeSketchColorizationDatasetGenerator:

    def __init__(self, type: str = 'ENV') -> None:
        self._kaggle_id = ANIME_SKETCH_COLORIZATION_DATASET_KAGGLE_ID
        self._dataset_id = ANIME_SKETCH_COLORIZATION_DATASET_DATASET_ID
        self._target_dataset = get_kaggle_dataset_id(self._kaggle_id,
                                                     self._dataset_id)
        self._fetch_kaggle_dataset_args = [
            'kaggle', 'datasets', 'download', self._target_dataset
        ]
        self._data_dir = get_data_root(type)
        create_dir_if_not_exist(self._data_dir)
        self._zipfile_location = get_zipfile_location(self._data_dir,
                                                      self._dataset_id)
        self._extract_location = get_extract_location(self._data_dir,
                                                      self._dataset_id)
        self._logger = logging.getLogger()
        self._kaggle_credential = get_kaggle_credential()
        maybe_fetch_kaggle_dataset(self._data_dir, self._kaggle_id,
                                   self._dataset_id, self._kaggle_credential)
        maybe_extract_kaggle_dataset(self._extract_location,
                                     self._zipfile_location)
        self._training_dataset_root = os.path.join(self._extract_location,
                                                   'data', 'train')
        self._logger.info('Use {root} as the training dataset root.'.format(
            root=self._training_dataset_root))
        self._training_data_files_gen = Path(
            self._training_dataset_root).glob('*.png')
        self._training_data_files = []
        for training_data_file in self._training_data_files_gen:
            self._training_data_files.append(training_data_file)
        self._logger.info('Found {cnt} training sample files.'.format(
            cnt=len(self._training_data_files)))
        self._tf_dataset = tf.data.Dataset.from_generator(
            self.image_data_generator,
            output_signature=(tf.TensorSpec(shape=(256, 256, 3),
                                            dtype=tf.float32),
                              tf.TensorSpec(shape=(256, 256, 3),
                                            dtype=tf.float32)))

    def get_tf_dataset(self):
        return self._tf_dataset

    def image_data_generator(self):
        for training_data_file in self._training_data_files:
            pixels = img_to_array(
                load_img(training_data_file, target_size=(256, 512)))
            color_img, bw_img = normalize_image(
                pixels[:, :256]), normalize_image(pixels[:, 256:])
            yield color_img, bw_img
