import argparse

from gaas.config import global_logger

parser = argparse.ArgumentParser(description='CLI utilities for GAAS')

generate_mini_dataset_opts = parser.add_argument_group('Generate mini dataset')
generate_mini_dataset_opts.add_argument('--app',
                                        type=str,
                                        required=True,
                                        help='The name of the application.')


def main():
    args = parser.parse_args()
    global_logger.info(args)
    global_logger.info('Done.')


if __name__ == '__main__':
    main()
