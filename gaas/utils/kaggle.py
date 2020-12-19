import os


def get_kaggle_dataset_id(kaggle_id: str, dataset_id: str) -> str:
    return '{kaggle_id}/{dataset_id}'.format(kaggle_id=kaggle_id,
                                             dataset_id=dataset_id)


def get_zipfile_location(data_root: str, dataset_id: str) -> str:
    zipfile_filename = '{filename}.zip'.format(filename=dataset_id)
    return os.path.join(data_root, zipfile_filename)


def get_extract_location(data_root: str, dataset_id: str) -> str:
    return os.path.join(data_root, dataset_id)
