import os
import zipfile
from subprocess import PIPE, Popen

from gaas.applications.image_coloring.config import (
    ANIME_SKETCH_COLORIZATION_DATASET_DATASET_ID,
    ANIME_SKETCH_COLORIZATION_DATASET_KAGGLE_ID)
from gaas.config import (KAGGLE_KEY_ENV_ID, KAGGLE_USERNAME_ENV_ID,
                         global_logger)


class KaggleCredential:

    def __init__(self, username: str, key: str) -> None:
        self.username = username
        self.key = key


def maybe_extract_kaggle_dataset(extract_location: str,
                                 zipfile_location: str) -> None:
    if os.path.exists(extract_location):
        global_logger.warn('The {dest} directory already exist. Skip.'.format(
            dest=extract_location))
        return
    with zipfile.ZipFile(zipfile_location, 'r') as zip_ref:
        zip_ref.extractall(extract_location)
    global_logger.info('Extract dataset done.')


def maybe_fetch_kaggle_dataset(data_root: str, kaggle_id: str, dataset_id: str,
                               kaggle_credential: KaggleCredential) -> None:
    kaggle_id = ANIME_SKETCH_COLORIZATION_DATASET_KAGGLE_ID
    dataset_id = ANIME_SKETCH_COLORIZATION_DATASET_DATASET_ID
    target_dataset = get_kaggle_dataset_id(kaggle_id, dataset_id)
    fetch_kaggle_dataset_args = [
        'kaggle', 'datasets', 'download', target_dataset
    ]
    fork_env = os.environ
    fork_env[KAGGLE_USERNAME_ENV_ID] = kaggle_credential.username
    fork_env[KAGGLE_KEY_ENV_ID] = kaggle_credential.key
    proc = Popen(fetch_kaggle_dataset_args,
                 cwd=data_root,
                 env=fork_env,
                 stdin=PIPE,
                 stdout=PIPE,
                 stderr=PIPE)
    _, stderr = proc.communicate()
    if proc.returncode != 0:
        global_logger.error(
            'Fetch dataset from Kaggle failed with return code {ret}'.format(
                ret=proc.returncode))
        global_logger.error('Error message: {msg}'.format(msg=stderr))
        raise RuntimeError('Fetch Kaggle dataset failed.')
    global_logger.info('Fetch Kaggle dataset done.')


def get_kaggle_dataset_id(kaggle_id: str, dataset_id: str) -> str:
    return '{kaggle_id}/{dataset_id}'.format(kaggle_id=kaggle_id,
                                             dataset_id=dataset_id)


def get_zipfile_location(data_root: str, dataset_id: str) -> str:
    zipfile_filename = '{filename}.zip'.format(filename=dataset_id)
    return os.path.join(data_root, zipfile_filename)


def get_extract_location(data_root: str, dataset_id: str) -> str:
    return os.path.join(data_root, dataset_id)
