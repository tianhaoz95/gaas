import os
from gaas.config import ROOT_DIR


def test_root_dir():
    """
    Check if the root directory is correct by checking if
    requirements.txt exist in the directory. This file needs
    to change of the location of requirements.txt changes in
    refactoring.
    """
    assert os.path.exists(os.path.join(ROOT_DIR, 'requirements.txt'))
