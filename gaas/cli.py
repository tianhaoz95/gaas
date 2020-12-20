import argparse

from gaas.applications.image_coloring.utils.fetch_dataset import \
    fetch_image_coloring_dataset
from gaas.applications.image_coloring.utils.generate_mini_dataset import \
    generate_mini_dataset
from gaas.config import global_logger
from gaas.utils.github import show_kaggle_credential

parser = argparse.ArgumentParser(description='CLI utilities for GAAS')

parser.add_argument('--app', type=str, help='The name of the application.')
parser.add_argument('--action',
                    type=str,
                    required=True,
                    help='The action to execute.')


def main():
    args = parser.parse_args()
    global_logger.info(args)
    if args.action == 'fetch_kaggle_credential':
        show_kaggle_credential()
    if args.action == 'fetch_kaggle_dataset':
        if args.app == 'image_coloring':
            fetch_image_coloring_dataset()
    if args.action == 'generate_mini_dataset':
        if args.app == 'image_coloring':
            generate_mini_dataset()
    global_logger.info('Done.')


if __name__ == '__main__':
    main()
