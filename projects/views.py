from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import ProjectSerializer
from core.models import Project


class ProjectAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class SingleProjectAPIView(RetrieveAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
