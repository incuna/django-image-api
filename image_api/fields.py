from imagekit.cachefiles import ImageCacheFile
from imagekit.registry import generator_registry
from imagekit.templatetags.imagekit import DEFAULT_THUMBNAIL_GENERATOR

from rest_framework import serializers


class ThumbnailNamedField(serializers.Field):
    """A field that returns a thumbnail of an named image field."""

    def __init__(self, image_field_name, generator_id=DEFAULT_THUMBNAIL_GENERATOR, **kwargs):
        self.image_field_name = image_field_name
        self.generator_id = generator_id
        self.kwargs = kwargs
        super(ThumbnailNamedField, self).__init__()

    def _generate_thumbnail(self, source, **kwargs):
        generator = generator_registry.get(
            DEFAULT_THUMBNAIL_GENERATOR,
            source=source,
            **kwargs)
        return ImageCacheFile(generator)

    def _get_image(self, obj):
        return getattr(obj, self.image_field_name)

    def field_to_native(self, obj, field_name):
        image = self._get_image(obj)
        if not image.name:
            return None
        if self.kwargs.get('width') or self.kwargs.get('height'):
            image = self._generate_thumbnail(image, **self.kwargs)

        value = image.url
        request = self.context.get('request', None)
        if request is not None:
            value = request.build_absolute_uri(value)

        return self.to_native(value)
