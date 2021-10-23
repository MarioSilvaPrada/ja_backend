from rest_framework.generics import ListAPIView

from .serializers import TagSerializer
from core.models import Tag


class TagAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
