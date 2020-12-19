import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)
global_logger = logging.getLogger()

# This is used to define the root directory of the project.
# If the location of this file changes, the implementation
# of the ROOT_DIR needs to change accordingly as well.
ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent

# Locations for datasets.
DATA_DIR = os.path.join(ROOT_DIR, 'data')
PROD_DATA_DIR = os.path.join(DATA_DIR, 'prod')
DEV_DATA_DIR = os.path.join(DATA_DIR, 'dev')
