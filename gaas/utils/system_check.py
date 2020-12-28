import tensorflow as tf
from gaas.config import global_logger


def run_system_check():
    gpus = tf.config.list_physical_devices("GPU")
    global_logger.info('Found {cnt} GPU devices.'.format(cnt=len(gpus)))
    global_logger.info(gpus)
