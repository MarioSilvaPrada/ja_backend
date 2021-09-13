from rest_framework.generics import ListAPIView

from .serializers import SettingsSerializer
from core.models import Settings

class SettingsAPIView(ListAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
