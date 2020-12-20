from gaas.applications.image_coloring.dataset import \
    AnimeSketchColorizationDatasetGenerator
from gaas.config import global_logger


def fetch_image_coloring_dataset():
    _ = AnimeSketchColorizationDatasetGenerator(type='PROD')
    global_logger.info('Fetch image coloring dataset. Done.')
