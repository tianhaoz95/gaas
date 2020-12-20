import argparse


def register_cli_options(parser: argparse.ArgumentParser) -> None:
    """
    This is a early stage idea where instead of defining a top-level
    CLI option set. We push the responsibility down to each applications.
    """
    app = parser.add_argument_group('Image Coloring Application')
    app.add_argument('--action',
                     type=str,
                     required=True,
                     help='The action to execute.')
