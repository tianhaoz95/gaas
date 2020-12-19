from gaas.applications.image_coloring.dataset import AnimeSketchColorizationDatasetGenerator


class AnimeColorizationDatasetTests:

    def test_init_without_error(self):
        gen = AnimeSketchColorizationDatasetGenerator()
        assert gen is not None
