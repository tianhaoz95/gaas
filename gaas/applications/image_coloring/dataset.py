import logging
import os
import zipfile
from subprocess import PIPE, Popen

from gaas.applications.image_coloring.config import (
    ANIME_SKETCH_COLORIZATION_DATASET_DATASET_ID,
    ANIME_SKETCH_COLORIZATION_DATASET_KAGGLE_ID)
from gaas.utils.exec_mode import get_data_root
from gaas.utils.filesys import create_dir_if_not_exist
from gaas.utils.github import get_kaggle_credential
from gaas.utils.kaggle import (get_extract_location, get_kaggle_dataset_id,
                               get_zipfile_location, maybe_fetch_kaggle_dataset)


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
        # self._maybe_fetch_kaggle_dataset()
        self._kaggle_credential = get_kaggle_credential()
        maybe_fetch_kaggle_dataset(self._data_dir, self._kaggle_id,
                                   self._dataset_id, self._kaggle_credential)
        self._maybe_extract_kaggle_dataset()

    def _maybe_fetch_kaggle_dataset(self) -> None:
        proc = Popen(self._fetch_kaggle_dataset_args,
                     cwd=self._data_dir,
                     stdin=PIPE,
                     stdout=PIPE,
                     stderr=PIPE)
        _, stderr = proc.communicate()
        if proc.returncode != 0:
            self._logger.error(
                'Fetch dataset from Kaggle failed with return code {ret}'.
                format(ret=proc.returncode))
            self._logger.error('Error message: {msg}'.format(msg=stderr))
            if 'KAGGLE_USERNAME' not in os.environ:
                self._logger.warn(
                    'KAGGLE_USERNAME not found in the environment.')
            if 'KAGGLE_KEY' not in os.environ:
                self._logger.warn('KAGGLE_KEY not found in the environment.')
            raise RuntimeError('Fetch Kaggle dataset failed.')
        self._logger.info('Fetch Kaggle dataset done.')

    def _maybe_extract_kaggle_dataset(self) -> None:
        if os.path.exists(self._extract_location):
            self._logger.warn(
                'The {dest} directory already exist. Skip.'.format(
                    dest=self._extract_location))
            return
        with zipfile.ZipFile(self._zipfile_location, 'r') as zip_ref:
            zip_ref.extractall(self._extract_location)
        self._logger.info('Extract dataset done.')
