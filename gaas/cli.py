import argparse

from gaas.applications.image_coloring.train import train_image_coloring
from gaas.applications.image_coloring.utils.fetch_dataset import \
    fetch_image_coloring_dataset
from gaas.applications.image_coloring.utils.generate_mini_dataset import \
    generate_mini_dataset
from gaas.config import (DEFAULT_TRAINING_BATCH_SIZE, DEFAULT_TRAINING_EPOCH,
                         global_logger)
from gaas.utils.github import show_kaggle_credential
from gaas.utils.system_check import run_system_check

parser = argparse.ArgumentParser(description='CLI utilities for GAAS')

parser.add_argument('--app', type=str, help='The name of the application.')
parser.add_argument('--action',
                    type=str,
                    required=True,
                    help='The action to execute.')
parser.add_argument('--epoch',
                    type=int,
                    required=False,
                    default=DEFAULT_TRAINING_EPOCH,
                    help='The epoch to train the model with.')
parser.add_argument('--batch_size',
                    type=int,
                    required=False,
                    default=DEFAULT_TRAINING_BATCH_SIZE,
                    help='The batch size to train the model with.')


def main():
    args = parser.parse_args()
    global_logger.info(args)
    if args.action == 'train':
        if args.app == 'image_coloring':
            train_image_coloring(epoch=args.epoch, batch_size=args.batch_size)
    if args.action == 'system_check':
        run_system_check()
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
