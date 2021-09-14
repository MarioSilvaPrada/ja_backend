from rest_framework.generics import ListAPIView

from .serializers import PartnersSerializer
from core.models import Partners

class PartnersAPIView(ListAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
