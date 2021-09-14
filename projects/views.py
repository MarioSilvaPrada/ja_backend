from rest_framework.generics import ListAPIView

from .serializers import ProjectSerializer
from core.models import Project

class ProjectAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
