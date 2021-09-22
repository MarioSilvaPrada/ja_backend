
from rest_framework import serializers
from core.models import Project, ProjectSection, Image


class ProjectImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class ProjectSectionSerializer(serializers.ModelSerializer):
    image = serializers.StringRelatedField(many=True)

    class Meta:
        model = ProjectSection
        fields = ['id', 'project', 'section_name', 'description', 'image']


class ProjectSerializer(serializers.ModelSerializer):
    
    section = ProjectSectionSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'main_image', 'section']
