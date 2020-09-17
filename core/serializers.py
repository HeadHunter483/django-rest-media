from rest_framework.serializers import ModelSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Image


class ImageSerializer(ModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50'),
        ],
    )

    class Meta:
        model = Image
        fields = [
            'id', 'creator', 'title', 'image', 'created_at', 'modified_at',
        ]
        read_only_fields = [
            'id', 'creator', 'image', 'created_at', 'modified_at',
        ]
