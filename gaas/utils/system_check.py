import tensorflow as tf


def run_system_check():
    gpus = tf.config.list_physical_devices("GPU")
    print(gpus)
