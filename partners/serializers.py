
from rest_framework import serializers
from core.models import Partners


class PartnersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partners
        fields = '__all__'
