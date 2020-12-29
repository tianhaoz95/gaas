from typing import Tuple

import tensorflow as tf
from gaas.applications.image_coloring.dataset import \
    AnimeSketchColorizationDatasetGenerator
from gaas.applications.image_coloring.model import (
    ImageColoringDiscriminatorModel, ImageColoringGanModel,
    ImageColoringGeneratorModel)
from gaas.config import global_logger
from tensorflow.keras.models import Model


def get_real_samples(dataset: tf.data.Dataset,
                     batch_size: int) -> Tuple[tf.Tensor, tf.Tensor, tf.Tensor]:
    batch = list(dataset.take(1))[0]
    color_batch = batch[0]
    bw_batch = batch[1]
    y_batch = tf.ones((batch_size, 1))
    return color_batch, bw_batch, y_batch


def get_fake_samples(generator: Model, bw_samples: tf.Tensor,
                     batch_size: int) -> Tuple[tf.Tensor, tf.Tensor]:
    color_samples = generator(bw_samples)
    y_batch = tf.zeros((batch_size, 1))
    return color_samples, y_batch


def train_image_coloring(epoch: int, batch_size: int) -> None:
    dataset_gen = AnimeSketchColorizationDatasetGenerator()
    tf_dataset = dataset_gen.get_tf_dataset().batch(batch_size,
                                                    drop_remainder=True)
    generator = ImageColoringGeneratorModel()
    discriminator = ImageColoringDiscriminatorModel()
    gan = ImageColoringGanModel(generator, discriminator)
    for _ in range(epoch):
        real_color_batch, real_bw_batch, real_y_batch = get_real_samples(
            tf_dataset, batch_size)
        fake_color_samples, fake_y_batch = get_fake_samples(
            generator, real_bw_batch, batch_size)
        d_loss_real = discriminator.train_on_batch(
            [real_color_batch, real_bw_batch], real_y_batch)
        d_loss_fake = discriminator.train_on_batch(
            [fake_color_samples, real_bw_batch], fake_y_batch)
    global_logger.info('Training done.')
