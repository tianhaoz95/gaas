import argparse

from gaas.applications.image_coloring.utils.generate_mini_dataset import \
    generate_mini_dataset
from gaas.config import global_logger
from gaas.utils.github import get_kaggle_credential

parser = argparse.ArgumentParser(description='CLI utilities for GAAS')

parser.add_argument('--app',
                    type=str,
                    required=True,
                    help='The name of the application.')


def main():
    args = parser.parse_args()
    global_logger.info(args)
    if parser.command == 'generate_mini_dataset':
        generate_mini_dataset()
    global_logger.info('Done.')


if __name__ == '__main__':
    main()
