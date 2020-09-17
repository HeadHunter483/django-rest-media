from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Image
from .serializers import ImageSerializer
from accounts.permissions import IsCreatorOrReadOnly


class ImageViewSet(NestedViewSetMixin, ModelViewSet):
    permission_classes = [IsCreatorOrReadOnly]
    queryset = Image.objects.all().order_by('-created_at')
    serializer_class = ImageSerializer
