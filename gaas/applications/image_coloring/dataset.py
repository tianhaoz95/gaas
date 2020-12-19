import logging
import os
import zipfile
from subprocess import PIPE, Popen

from gaas.applications.image_coloring.config import \
    ANIME_SKETCH_COLORIZATION_DATASET_KAGGLE_ID
from gaas.config import DATA_DIR


class AnimeSketchColorizationDatasetGenerator:

    def __init__(self) -> None:
        self._kaggle_id = ANIME_SKETCH_COLORIZATION_DATASET_KAGGLE_ID
        self._dataset_id = 'anime-sketch-colorization-pair'
        self._target_dataset = '{kaggle_id}/{dataset_id}'.format(
            kaggle_id=self._kaggle_id, dataset_id=self._dataset_id)
        self._fetch_kaggle_dataset_args = [
            'kaggle', 'datasets', 'download', self._target_dataset
        ]
        self._zipfile_filename = '{filename}.zip'.format(
            filename=self._dataset_id)
        self._zipfile_location = os.path.join(DATA_DIR, self._zipfile_filename)
        self._extract_location = os.path.join(DATA_DIR, self._dataset_id)
        self._logger = logging.getLogger()
        self._maybe_fetch_kaggle_dataset()
        self._maybe_extract_kaggle_dataset()

    def get_dataset_location(self) -> str:
        return self._extract_location

    def _maybe_fetch_kaggle_dataset(self) -> None:
        proc = Popen(self._fetch_kaggle_dataset_args,
                     cwd=DATA_DIR,
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
