from gaas.applications.image_coloring.model import (
    ImageColoringGeneratorEncoderBlock, ImageColoringGeneratorDecoderBlock,
    ImageColoringGeneratorModel, ImageColoringDiscriminatorModel)


class ImageColoringGeneratorEncoderBlockTests:

    def test_init_without_error(self):
        model = ImageColoringGeneratorEncoderBlock()
        assert model is not None

    def test_foward_pass_without_error(self):
        pass

    def test_backward_pass_without_error(self):
        pass


class ImageColoringGeneratorDecoderBlockTests:

    def test_init_without_error(self):
        model = ImageColoringGeneratorDecoderBlock()
        assert model is not None

    def test_foward_pass_without_error(self):
        pass

    def test_backward_pass_without_error(self):
        pass


class ImageColoringGeneratorModelTests:

    def test_init_without_error(self):
        model = ImageColoringGeneratorModel()
        assert model is not None

    def test_foward_pass_without_error(self):
        pass

    def test_backward_pass_without_error(self):
        pass


class ImageColoringDiscriminatorModelTests:

    def test_init_without_error(self):
        model = ImageColoringDiscriminatorModel()
        assert model is not None

    def test_foward_pass_without_error(self):
        pass

    def test_backward_pass_without_error(self):
        pass