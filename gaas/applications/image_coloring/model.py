from tensorflow.keras.models import Model


class ImageColoringGeneratorEncoderBlock(Model):

    def __init__(self):
        super(ImageColoringGeneratorEncoderBlock, self).__init__()

    def call(self, x):
        # TODO: Port the forward pass for encoder block
        #   This is similar to the define_encoder_block in the post.
        #   However, it will be converted to TF2 style.
        pass


class ImageColoringGeneratorDecoderBlock(Model):

    def __init__(self):
        super(ImageColoringGeneratorDecoderBlock, self).__init__()

    def call(self, x):
        # TODO: Port the forward pass for decoder block
        #   This is similar to the decoder_block in the post.
        #   However, it will be converted to TF2 style.
        pass


class ImageColoringGeneratorModel(Model):

    def __init__(self):
        super(ImageColoringGeneratorModel, self).__init__()

    def call(self, x):
        # TODO: Port the forward pass for generator
        #   This is similar to the define_generator in the post.
        #   However, it will be converted to TF2 style.
        pass


class ImageColoringDiscriminatorModel(Model):

    def __init__(self):
        super(ImageColoringDiscriminatorModel, self).__init__()

    def call(self, x):
        # TODO: Port the forward pass for discriminator
        #   This is similar to the define_discriminator in the post.
        #   However, it will be converted to TF2 style.
        pass
