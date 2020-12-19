import os
import uuid
import zipfile

from gaas.utils.filesys import recreate_dir


def create_dummy_zipfile(filename: str,
                         temp: str = '/tmp/gaas/testing',
                         file_cnt: int = 10) -> None:
    recreate_dir(temp)
    dummy_files = []
    for _ in range(file_cnt):
        dummy_filename = '{random_file}.txt'.format(random_file=uuid.uuid1())
        dummy_file = os.path.join(temp, dummy_filename)
        with open(dummy_file, 'w+') as _:
            pass
        dummy_files.append(dummy_file)
    dummy_zipfile = zipfile.ZipFile(filename, mode='w')
    try:
        for dummy_file in dummy_files:
            dummy_zipfile.write(dummy_file)
    finally:
        dummy_zipfile.close()
