from tensorflow.keras.models import Model


class ImageColoringGeneratorEncoderBlock(Model):

    def __init__(self):
        super(ImageColoringGeneratorEncoderBlock, self).__init__()

    def call(self, x):
        # TODO Implement the forward pass for encoder block
        #   This is similar to the define_encoder_block in the post.
        #   assignees: emzak208
        pass


class ImageColoringGeneratorDecoderBlock(Model):

    def __init__(self):
        super(ImageColoringGeneratorDecoderBlock, self).__init__()

    def call(self, x):
        pass


class ImageColoringGeneratorModel(Model):

    def __init__(self):
        super(ImageColoringGeneratorModel, self).__init__()

    def call(self, x):
        pass


class ImageColoringDiscriminatorModel(Model):

    def __init__(self):
        super(ImageColoringDiscriminatorModel, self).__init__()

    def call(self, x):
        pass
