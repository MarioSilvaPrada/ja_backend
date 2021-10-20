from rest_framework.generics import ListAPIView

from .serializers import AboutSerializer
from core.models import About


class AboutAPIView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
