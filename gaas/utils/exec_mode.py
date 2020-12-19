import os

from gaas.config import DEV_DATA_DIR, PROD_DATA_DIR


def get_data_root(type) -> str:
    if type == 'DEV':
        return DEV_DATA_DIR
    elif type == 'PROD':
        return PROD_DATA_DIR
    elif type == 'ENV':
        if 'CI' in os.environ and os.environ['CI'] == 'true':
            return DEV_DATA_DIR
        return PROD_DATA_DIR
    else:
        raise RuntimeError(
            'Override option {override} not supported.'.format(override=type))
