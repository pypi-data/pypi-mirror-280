from mirp.settings.generic import SettingsClass
from mirp._images.generic_image import GenericImage


class GenericFilter:

    def __init__(self, settings: SettingsClass, name: str):
        # In-slice (2D) or 3D filtering
        self.by_slice = settings.img_transform.by_slice

    def generate_object(self):
        raise NotImplementedError("_generate_object method should be defined in the subclasses")

    def transform(self, image: GenericImage):
        raise NotImplementedError("transform method should be defined in the subclasses.")
